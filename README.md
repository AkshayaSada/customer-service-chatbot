# 🤖 Customer Service Chatbot

A lightweight, intent-based customer service chatbot built with **Python**, **NLTK**, **Scikit-learn**, and **Streamlit**. It uses Machine Learning to recognize customer queries and return relevant responses in a real-time web UI.

---

## 🚀 Features

- **Intent Recognition:** Classifies user messages into distinct categories (Shipping, Returns, Refunds, Order Status, Payment Issues, etc.).
- **NLP Pipeline:** Text normalization with tokenization, lemmatization, and TF-IDF feature extraction.
- **Machine Learning Engine:** Driven by a Logistic Regression model with a confidence threshold fallback for unrecognized inputs.
- **Interactive UI:** Built with Streamlit's native chat UI (`st.chat_input` and `st.chat_message`).

---

## 🏗️ Architecture Flow

```text
User Message
     │
     ▼
Text Preprocessing (Lowercasing, Punctuation Removal, Lemmatization)
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Logistic Regression Classifier
     │
     ▼
Intent Prediction & Probability Threshold Check
     │
     ▼
Selected Response Output
