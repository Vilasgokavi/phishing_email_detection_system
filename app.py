import pandas as pd
import numpy as np
import re
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from nltk.corpus import stopwords
from urllib.parse import urlparse
import requests
import nltk

# Download NLTK stopwords
nltk.download('stopwords')
STOPWORDS = set(stopwords.words("english"))

# Email cleaning
def clean_email_body(email_body):
    email_body = re.sub(r'[^a-zA-Z\s]', '', email_body)
    email_body = ' '.join([word.lower() for word in email_body.split() if word.lower() not in STOPWORDS])
    return email_body

# URL feature extraction
def extract_url_features(email_body):
    urls = re.findall(r'(https?://[^\s]+)', email_body)
    features = []
    for url in urls:
        parsed_url = urlparse(url)
        domain_length = len(parsed_url.netloc)
        path_length = len(parsed_url.path)
        protocol = parsed_url.scheme
        features.extend([domain_length, path_length, 1 if protocol in ['http', 'https'] else 0])
        try:
            response = requests.get(url, timeout=3)
            features.append(response.status_code)
        except:
            features.append(0)
    return np.mean([f for f in features if isinstance(f, (int, float))]) if features else 0

# Train model
def train_model(data):
    data['cleaned_body'] = data['email_body'].apply(clean_email_body)
    data['url_features'] = data['email_body'].apply(extract_url_features)

    X = pd.concat([data['cleaned_body'], data['url_features']], axis=1)
    X.columns = ['email_body', 'url_features']
    y = data['label']

    vectorizer = CountVectorizer()
    model = make_pipeline(vectorizer, MultinomialNB())
    model.fit(X['email_body'], y)
    joblib.dump(model, 'phishing_model.pkl')

# Predict spam or ham
def predict_spam_ham(model, email_body):
    cleaned_body = clean_email_body(email_body)
    url_features = extract_url_features(email_body)
    X = pd.DataFrame([[cleaned_body, url_features]], columns=['email_body', 'url_features'])
    prediction = model.predict(X['email_body'])
    return 'Spam' if prediction[0] == 1 else 'Ham'

# Streamlit app
def main():
    st.set_page_config(page_title="Spam Detector", layout="centered")
    st.image("phishing.png", width=700)

    # Force single-line title
    st.markdown(
        "<h1 style='white-space: nowrap;'>📧 Phishing Email Detection System</h1>",
        unsafe_allow_html=True
    )

    # Load model
    model = None
    try:
        model = joblib.load('phishing_model.pkl')
    except:
        st.warning("⚠️ No trained model found. Upload data below to train.")

    # Email input
    st.subheader("🔍 Analyze Email Content")
    email_input = st.text_area("Enter the Email Body Here:", height=200)

    if st.button("🔎 Detect Spam or Ham"):
        if email_input.strip() == "":
            st.error("Please enter some email text for analysis.")
        elif model is None:
            st.error("Model not loaded. Please upload training data to train the model.")
        else:
            result = predict_spam_ham(model, email_input)
            if result == 'Spam':
                st.error("🚨 This email is classified as **SPAM**.")
            else:
                st.success("✅ This email is classified as **HAM** (Safe).")

    # Training section
    st.markdown("---")
    st.subheader("🛠️ Train the Model (Optional)")
    uploaded_file = st.file_uploader("Upload a CSV file with 'email_body' and 'label' columns", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        if 'email_body' in data.columns and 'label' in data.columns:
            with st.spinner("Training the model..."):
                train_model(data)
                st.success("✅ Model trained and saved successfully! Please refresh to reload.")
        else:
            st.error("❌ CSV must contain 'email_body' and 'label' columns.")

if __name__ == '__main__':
    main()
