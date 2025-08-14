
<h1 align="center">📧 Phishing Email Detection System</h1>

<p align="center">
  <img src="phishing.png" alt="Phishing Detection Banner" width="700">
</p>

---

## 📌 Overview

**`Phishing Email Detection System`** is an AI-based tool to detect phishing and spam emails using **machine learning** and **NLP**. The system classifies emails as **Spam** (phishing) or **Ham** (safe) and provides an intuitive **Streamlit interface** for testing and training.

---

## 🧠 Features

- 📝 **Text Cleaning** — Removes stopwords and unnecessary symbols using NLTK.
- 🔗 **URL Feature Extraction** — Extracts domain length, path length, HTTP response codes.
- 🧠 **Machine Learning Pipeline** — Trains a Naive Bayes model with vectorized input.
- 💻 **Streamlit Frontend** — Easy-to-use web app for real-time predictions.
- 📁 **Model Retraining** — Upload your own dataset (`email_body`, `label`) to build a new model.

---

## 🧑‍💻 Tech Stack

| Component     | Tools Used                                |
|---------------|--------------------------------------------|
| Language      | Python 3                                   |
| Web Interface | Streamlit                                  |
| ML Model      | scikit-learn (Naive Bayes)                 |
| Text Processing | nltk, re                                |
| HTTP Requests | requests                                   |
| Data Handling | pandas                                     |
| Serialization | joblib                                     |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Vilasgokavi/phishing_email_detection_system.git
cd phishing_email_detection_system
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📝 How to Use

1. **Test Email Text**  
   - Paste any email content into the input box.  
   - Click "Detect Spam or Ham" to get the result.

2. **Train Your Own Model** *(Optional)*  
   - Upload a `.csv` file with:
     - `email_body`: The content of the email  
     - `label`: `1` for spam, `0` for safe  
   - Model will be retrained and saved as `phishing_model.pkl`.

3. **Check Results**  
   - The output will tell you if the email is **Spam** (phishing) or **Ham** (safe).

---

## 📁 Project Structure

```
phishing_email_detection_system/
│
├── app.py                 # Main Streamlit application
├── phishing_model.pkl     # Pre-trained ML model
├── emails.csv             # Sample dataset for training
├── phishing.png           # Banner image
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ✉️ Sample Email Inputs

### 🚨 Spam Email
```
Subject: Win a Free iPhone Now!
You’ve been selected for a $1000 gift card. Click here: http://phishing-scam.com
```

### ✅ Safe Email
```
Subject: Meeting Reminder
Hi, just checking in about tomorrow's project sync. Let me know your availability.
```

---

## 🖼️ Output Preview

### Application Screens

| Home Page | Spam Detection | Ham Detection |
|-----------|----------------|---------------|
| ![Home Interface](https://github.com/Vilasgokavi/phishing_email_detection_system/raw/main/home.png) | ![Spam Example](https://github.com/Vilasgokavi/phishing_email_detection_system/raw/main/spam.png) | ![Ham Example](https://github.com/Vilasgokavi/phishing_email_detection_system/raw/main/ham.png) |

### Model Training
![Training Interface](https://github.com/Vilasgokavi/phishing_email_detection_system/raw/main/train.png)


---

## 🤝 Contributing

Contributions are welcome!  
To contribute:
1. Fork this repo.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

---


## 👤 Developer Info

**Vilas Gokavi**  
📧 Email: [vilasgokavi@gmail.com](mailto:vilasgokavi@gmail.com)  
💼 LinkedIn: [linkedin.com/in/vilas-gokavi](https://www.linkedin.com/in/vilas-gokavi)  
💻 GitHub: [github.com/Vilasgokavi](https://github.com/Vilasgokavi)

---

> 🚀 Empowering email security with machine learning and transparency.
