# 📩 SMS Spam Detection App

An end-to-end Machine Learning project that detects whether a message is **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) and a deployed Streamlit web application.

---

## 🚀 Project Overview

This project aims to identify spam messages by analyzing text content using machine learning techniques. It covers the complete pipeline from data preprocessing to model deployment.

---

## ✨ Features

- 📩 Classifies SMS messages as Spam or Not Spam  
- 🧠 NLP-based text preprocessing (tokenization, stopword removal, stemming)  
- 🔍 TF-IDF vectorization for feature extraction  
- 🤖 Machine Learning model for classification  
- 🌐 Interactive web app built with Streamlit  
- ⚡ Hybrid system (ML + keyword-based detection)  
- 📊 Displays prediction confidence  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- NLTK  
- Scikit-learn  
- Streamlit  

---

## 🔄 Workflow

1. Data Cleaning  
2. Text Preprocessing  
3. Feature Extraction (TF-IDF)  
4. Model Training & Evaluation  
5. Model Saving using Pickle  
6. Deployment using Streamlit  

---

## 📂 Project Structure

```
├── app.py
├── model.pkl
├── vectorizer.pkl
├── processed_spam.csv
├── model_build.ipynb
├── model_training.ipynb
```

---

## ▶️ How to Run Locally

### 1. Clone the Repository
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the App
```
streamlit run app.py
```

---

## 💡 Example

**Input:**
```
Click on this link and get 1000 rupees
```

**Output:**
```
🚨 Spam Message
```

---

## 🎯 Future Improvements

- Improve accuracy using advanced models (XGBoost, Deep Learning)  
- Add multilingual spam detection  
- Deploy application on cloud platforms  
- Enhance UI/UX  

---

## 🧠 Key Learnings

- Natural Language Processing (NLP)  
- Feature Engineering using TF-IDF  
- Machine Learning Model Development  
- Building and Deploying ML Applications  

---

## 👨‍💻 Author

Siddheya Pitambare
