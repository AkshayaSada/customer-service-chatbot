import json
import random
import re
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Download required NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

class IntentChatbot:
    def __init__(self, intents_filepath='data/intents.json'):
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer(tokenizer=self._preprocess, stop_words='english')
        self.classifier = LogisticRegression(max_iter=200)
        
        with open(intents_filepath, 'r') as file:
            self.intents_data = json.load(file)['intents']
            
        self._train_model()

    def _preprocess(self, text):
        text = re.sub(r'[^\w\s]', '', text.lower())
        tokens = nltk.word_tokenize(text)
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def _train_model(self):
        corpus = []
        labels = []
        
        for intent in self.intents_data:
            for pattern in intent['patterns']:
                corpus.append(pattern)
                labels.append(intent['tag'])
                
        X = self.vectorizer.fit_transform(corpus)
        self.classifier.fit(X, labels)

    def get_response(self, user_message, threshold=0.25):
        X_test = self.vectorizer.transform([user_message])
        probabilities = self.classifier.predict_proba(X_test)[0]
        max_idx = probabilities.argmax()
        
        if probabilities[max_idx] < threshold:
            return "I'm sorry, I didn't quite understand that. Could you rephrase your question?"

        predicted_intent = self.classifier.classes_[max_idx]
        
        for intent in self.intents_data:
            if intent['tag'] == predicted_intent:
                return random.choice(intent['responses'])

if __name__ == "__main__":
    bot = IntentChatbot()
    print("Bot initialized. Type 'exit' to quit.")
    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        print(f"Bot: {bot.get_response(msg)}")