
import streamlit as st
import pickle
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Preprocessing
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# UI
st.title("📰 Fake News Detector")
st.write("Paste a news headline or article and see if it's fake or real.")

user_input = st.text_area("Enter news text here:", height=200)

if st.button("Predict"):
    cleaned = preprocess(user_input)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    result = "🟥 FAKE News" if prediction == 0 else "🟩 REAL News"
    st.subheader("Result:")
    st.success(result)
