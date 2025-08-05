import streamlit as st
import pickle
import re

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Preprocessing function
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# Streamlit App
st.title("Fake News Detector")

input_text = st.text_area("Enter news article text:")

if st.button("Check"):
    cleaned = preprocess(input_text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    result = "REAL" if prediction == 1 else "FAKE"
    st.success(f"This news is likely: {result}")
