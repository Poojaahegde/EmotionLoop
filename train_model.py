import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("data/emotion_dataset.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["emotion"]

model = LogisticRegression()
model.fit(X, y)

with open("model/emotion_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully!")
