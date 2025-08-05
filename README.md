
# 📰 Fake News Detection Web App

I built a simple **fake news detection system** using machine learning and natural language processing.  
The idea was to create a tool that could read a news article and tell whether it’s likely to be **real or fake**.

I used a publicly available dataset from Kaggle containing real and fake news articles. After cleaning the text, I trained a **Logistic Regression model** using **TF-IDF** features, and it gave me around **90% accuracy**.

Then, to make it more interactive and easy to share, I turned the model into a **Streamlit web app**. Anyone can paste news text into the app, click a button, and instantly see if it’s real or fake — all from a browser.

This project helped me understand how text preprocessing, model training, and deployment work together — and it made me even more interested in using AI for solving real-world problems like misinformation.

## 🚀 How to Run
1. Upload the files to a GitHub repo
2. Go to https://streamlit.io/cloud
3. Sign in with GitHub, choose your repo, and deploy

## 🛠 Tech Used
- Python
- Streamlit
- Scikit-learn
- NLTK
- Pandas
