# EmotionLoop 💭 — Real-Time Emotion Detection for Product & UX Research

> **Detect emotions in user text — not just positive/negative, but joy, anger, fear, sadness, and surprise — to help PMs build more empathetic products.**
>
> [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org) [![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red.svg)](https://streamlit.io) [![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)](https://scikit-learn.org) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
>
> ---
>
> ## 🚀 Product Overview
>
> **The Problem:** Standard sentiment analysis tells you if feedback is positive or negative — but it doesn't tell you *why* or *what emotion is driving it*. A user saying "I can't believe this feature is gone" could be expressing anger, sadness, or surprise. These emotions require completely different product responses. Coarse sentiment scores miss this nuance.
>
> **The Solution:** EmotionLoop is a Streamlit app that classifies text into 6 discrete emotions (joy, sadness, anger, fear, surprise, neutral) using a trained ML classifier. It goes beyond binary sentiment to give PMs richer emotional signal from user feedback, support tickets, and research notes.
>
> **The Impact:**
> - 🎭 Detects **6 emotion categories** — far richer than binary positive/negative sentiment
> - - 🔍 Helps PMs identify **anger vs. disappointment vs. confusion** in user feedback
>   - - 📊 Enables **emotion-aware product decisions** — e.g., prioritize angry users vs. confused ones differently
>     - - 🧠 Demonstrates applied ML: **trained classifier** on real emotion-labeled data (not just rule-based)
>      
>       - ---
>
> ## 🎯 Why This Matters (Product Perspective)
>
> Empathy is a core PM skill — and emotion detection is empathy at scale. When a PM can say "23% of support tickets this week contain anger signals — primarily around the billing page," that's a product priority, not just a support issue. EmotionLoop demonstrates that NLP can extend human empathy to thousands of user interactions simultaneously.
>
> ---
>
> ## 🧠 AI/ML Explanation
>
> | Component | Technique | Why It Was Chosen |
> |---|---|---|
> | **Text Features** | TF-IDF Vectorization | Converts text to numerical features capturing word importance |
> | **Classifier** | Logistic Regression / SVM | Fast, interpretable, high accuracy on emotion classification tasks |
> | **Training Data** | Emotion-labeled text dataset | Supervised learning — model learns emotion signals from labeled examples |
> | **Emotion Classes** | Joy, Sadness, Anger, Fear, Surprise, Neutral | Standard 6-class emotion taxonomy used in affective computing research |
>
> **Why 6 classes instead of more?**
> More classes = more training data needed + lower accuracy per class. The 6-emotion taxonomy is the industry standard (Ekman's basic emotions) and maps directly to distinct product response strategies — e.g., angry users need immediate resolution; confused users need better UX.
>
> **Training Pipeline:**
> ```
> Raw text → TF-IDF vectorization → Train classifier → Predict emotion label + confidence
> ```
>
> ---
>
> ## 🛠 Tech Stack
>
> | Layer | Technology |
> |---|---|
> | UI | Streamlit |
> | ML Model | scikit-learn (TF-IDF + Logistic Regression) |
> | Model Training | Python (train_model.py) |
> | Data Processing | Pandas, NumPy |
> | Language | Python 3.8+ |
>
> ---
>
> ## 📊 Sample Results
>
> **Input:** *"I can't believe they removed the export feature — I used it every single day. This is so frustrating."*
>
> | Emotion | Confidence |
> |---|---|
> | **Anger** | **72.4%** ✅ |
> | Sadness | 18.1% |
> | Surprise | 6.3% |
> | Joy | 1.8% |
> | Fear | 0.9% |
> | Neutral | 0.5% |
>
> **Input:** *"Just discovered the new search feature — this is exactly what I needed!"*
>
> | Emotion | Confidence |
> |---|---|
> | **Joy** | **84.7%** ✅ |
> | Surprise | 9.2% |
> | Neutral | 4.1% |
>
> **PM Application:** Batch-analyze 200 support tickets → find that 40% contain anger signals about the billing page → escalate billing UX to P0 in next sprint.
>
> ---
>
> ## 📸 Demo Instructions
>
> ```bash
> # 1. Clone the repo
> git clone https://github.com/Poojaahegde/EmotionLoop.git
> cd EmotionLoop
>
> # 2. Install dependencies
> pip install -r requirements.txt
>
> # 3. Train the model (first-time setup)
> python train_model.py
>
> # 4. Launch the app
> streamlit run app.py
> ```
>
> Open **http://localhost:8501** in your browser. Type or paste any text to get instant emotion detection.
>
> ---
>
> ## 🎯 Product Thinking Layer
>
> ### 👥 Target Users
> - **Product Managers** analyzing emotion patterns across large volumes of user feedback
> - - **UX Researchers** understanding emotional responses to design decisions
>   - - **Customer Success Teams** triaging support tickets by emotional urgency (angry > confused > neutral)
>     - - **Marketing Teams** measuring emotional response to campaigns or product launches
>      
>       - ### 😣 Pain Points Solved
>       - 1. **Coarse sentiment is insufficient** — "negative" feedback lumps together anger, sadness, and confusion, which need different responses
>         2. 2. **Manual emotional analysis doesn't scale** — a PM can empathize with 10 users; emotion detection scales to 10,000
>            3. 3. **Missing urgency signals** — angry users churn fast; without detection, support teams prioritize by time, not emotional urgency
>              
>               4. ### 🧩 Key Product Decisions Made
>               5. - **6-class taxonomy over custom classes:** Standard taxonomy enables comparison with industry benchmarks and is well-validated by research
>                  - - **Confidence scores shown:** Not just the predicted emotion but how confident the model is — PMs need to know when to trust the output
>                    - - **Streamlit for PM accessibility:** PMs need to run this without engineering support; Streamlit provides that
>                      - - **Train locally (train_model.py) over API:** Data stays on-premise; sensitive user feedback shouldn't leave the organization
>                       
>                        - ### 🗺 Future Roadmap
>                        - | Priority | Feature | Expected Impact |
>                        - |---|---|---|
>                        - | P0 | Batch CSV processing — analyze 1000 feedback entries at once | Scale from demo to production use |
>                        - | P0 | Emotion trend dashboard — % of each emotion over time | Track emotional health of product experience |
>                        - | P1 | Fine-tuned BERT model for higher accuracy | Improve from ~75% to ~90%+ accuracy |
>                        - | P1 | Export emotion-tagged feedback to CSV | Share with team for sprint planning |
>                        - | P2 | Anger/urgency alert system — "12% anger spike detected this week" | Proactive PM notification |
>                        - | P2 | Integration with FeedbackSense — cluster + emotion in one view | Unified feedback intelligence dashboard |
>                        - | P3 | Real-time integration with Zendesk / Intercom | Live emotion scoring on incoming tickets |
>                       
>                        - ---
>
> ## 📁 Project Structure
>
> ```
> EmotionLoop/
> ├── app.py               # Streamlit UI — text input and emotion prediction display
> ├── train_model.py       # Model training script — TF-IDF + classifier pipeline
> ├── requirements.txt     # Python dependencies
> └── README.md            # This file
> ```
>
> ---
>
> ## 🔗 Related Projects in This Portfolio
> - [**FeedbackSense**](https://github.com/Poojaahegde/FeedbackSense-AI-Product-Feedback-Analyzer) — AI-powered user feedback clustering (pairs perfectly with EmotionLoop)
> - - [**ScopeCreep**](https://github.com/Poojaahegde/scopecreep) — Real-time scope drift detector for product teams
>  
>   - ---
>
> *Built as part of an AI PM portfolio — demonstrating how emotion-aware AI can help PMs build more empathetic, user-centered products.*
