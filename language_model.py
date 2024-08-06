import re
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import os
import sys

# Function to load and preprocess data
def load_data(file_path):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit()
    
    try:
        data = pd.read_csv(file_path)
        if "Text" not in data.columns or "Language" not in data.columns:
            print("The CSV file does not contain the required columns 'Text' and 'Language'.")
            sys.exit()
        return data
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        sys.exit()

# Read the CSV file
file_path = "balanced_lang_detect_dataset.csv"  # Since it's in the same directory, just use the file name
data = load_data(file_path)

X = data["Text"]
Y = data["Language"]
le = LabelEncoder()
Y_encoded = le.fit_transform(Y)
data_list = [re.sub(r'[^\w\s]', '', text).lower() for text in X]  # Only removing non-alphanumeric characters
cv = CountVectorizer(max_features=5000, stop_words='english')  # Adding stop_words to filter out common words
X_vectorized = cv.fit_transform(data_list).toarray()
x_train, x_test, y_train, y_test = train_test_split(X_vectorized, Y_encoded, test_size=0.20, random_state=42)
model = MultinomialNB()
model.fit(x_train, y_train)

def predict(text):
    try:
        text_cleaned = re.sub(r'[^\w\s]', '', text).lower()
        x = cv.transform([text_cleaned]).toarray()
        lang_pred = model.predict(x)
        lang_decoded = le.inverse_transform(lang_pred)
        return lang_decoded[0]
    except Exception as e:
        print(f"Prediction error: {e}")
        return "Error"
