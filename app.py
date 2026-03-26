import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Load saved model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

ps = PorterStemmer()

# Text preprocessing function (SAME as training)
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# 🔥 NEW: Suspicious keyword checker
def is_suspicious(text):
    spam_keywords = [
        "click", "link", "offer", "win", "free",
        "money", "urgent", "prize", "cash", "reward"
    ]
    return any(word in text.lower() for word in spam_keywords)

# UI
st.set_page_config(page_title="Spam Detector", page_icon="📩")

st.title("📩 SMS Spam Detection App")
st.write("Detect whether a message is Spam or Not Spam")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        # Preprocess
        transformed_sms = transform_text(input_sms)

        # Vectorize
        vector_input = tfidf.transform([transformed_sms])

        # Predict
        result = model.predict(vector_input)[0]

        # 🔥 NEW: Confidence score
        try:
            proba = model.predict_proba(vector_input)[0]
            confidence = max(proba) * 100
        except:
            confidence = None

        # 🔥 NEW: Hybrid decision
        if result == 1 or is_suspicious(input_sms):
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")

        # Show confidence
        if confidence:
            st.info(f"Confidence: {confidence:.2f}%")

        st.markdown("---")
        st.caption("Built using Machine Learning + Rule-Based Filtering")