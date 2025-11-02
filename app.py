import streamlit as st
import pickle
from utils.preprocess import clean_text
import numpy as np

with open("model/emotion_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="EmotionLoop", page_icon="💭", layout="centered")
st.title("💭 EmotionLoop — Understand What You Feel Through Words")
st.write("Type something below to detect its emotion:")

text = st.text_area("Your text here:")

if st.button("Analyze Emotion"):
    if text.strip():
        cleaned = clean_text(text)
        pred = model.predict([cleaned])[0]
        prob = np.max(model.predict_proba([cleaned])) * 100

        colors = {
            "joy": "green",
            "anger": "red",
            "sadness": "blue",
            "fear": "purple",
            "neutral": "gray"
        }
        emojis = {
            "joy": "😊",
            "anger": "😡",
            "sadness": "😢",
            "fear": "😨",
            "neutral": "😐"
        }

        st.markdown(
            f"<h3 style='color:{colors[pred]}; text-align:center;'>{emojis[pred]} {pred.capitalize()} ({prob:.1f}%)</h3>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter some text.")