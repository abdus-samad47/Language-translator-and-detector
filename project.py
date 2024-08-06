# This file contains whole code of the project (ignore it)


# import sys
# import re
# import pandas as pd
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit, QMessageBox, QComboBox
# from googletrans import Translator, LANGUAGES
# from sklearn.preprocessing import LabelEncoder
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB
# import os

# # Global Translator initialization
# translator = Translator()

# # Function to load and preprocess data
# def load_data(file_path):
#     if not os.path.isfile(file_path):
#         print(f"File not found: {file_path}")
#         sys.exit()
    
#     try:
#         data = pd.read_csv(file_path)
#         if "Text" not in data.columns or "Language" not in data.columns:
#             print("The CSV file does not contain the required columns 'Text' and 'Language'.")
#             sys.exit()
#         return data
#     except Exception as e:
#         print(f"An error occurred while reading the CSV file: {e}")
#         sys.exit()

# # Read the CSV file
# file_path = "balanced_lang_detect_dataset.csv"  # Since it's in the same directory, just use the file name
# data = load_data(file_path)

# X = data["Text"]
# Y = data["Language"]
# le = LabelEncoder()
# Y_encoded = le.fit_transform(Y)
# data_list = [re.sub(r'[^\w\s]', '', text).lower() for text in X]  # Only removing non-alphanumeric characters
# cv = CountVectorizer(max_features=5000, stop_words='english')  # Adding stop_words to filter out common words
# X_vectorized = cv.fit_transform(data_list).toarray()
# x_train, x_test, y_train, y_test = train_test_split(X_vectorized, Y_encoded, test_size=0.20, random_state=42)
# model = MultinomialNB()
# model.fit(x_train, y_train)

# def predict(text):
#     try:
#         text_cleaned = re.sub(r'[^\w\s]', '', text).lower()
#         x = cv.transform([text_cleaned]).toarray()
#         lang_pred = model.predict(x)
#         lang_decoded = le.inverse_transform(lang_pred)
#         return lang_decoded[0]
#     except Exception as e:
#         print(f"Prediction error: {e}")
#         return "Error"

# class LanguageTranslationSystem(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         layout = QVBoxLayout(self)
#         detect_btn = QPushButton('Detect Language', self)
#         detect_btn.clicked.connect(self.open_lang_detect_window)
#         translate_btn = QPushButton('Translate Text', self)
#         translate_btn.clicked.connect(self.open_translate_window)
#         exit_btn = QPushButton('Exit', self)
#         exit_btn.clicked.connect(self.close)
#         layout.addWidget(detect_btn)
#         layout.addWidget(translate_btn)
#         layout.addWidget(exit_btn)
#         self.setLayout(layout)
#         self.setGeometry(300, 300, 300, 200)

#     def open_translate_window(self):
#         self.translate_window = TranslateWindow()
#         self.translate_window.show()

#     def open_lang_detect_window(self):
#         self.lang_detect_window = LangDetectWindow()
#         self.lang_detect_window.show()

# class TranslateWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         layout = QVBoxLayout(self)
#         self.sourceLangCombo = QComboBox()
#         self.destLangCombo = QComboBox()
#         for lang_code, lang_name in sorted(LANGUAGES.items(), key=lambda x: x[1]):
#             self.sourceLangCombo.addItem(lang_name, lang_code)
#             self.destLangCombo.addItem(lang_name, lang_code)
#         self.sourceLangCombo.setCurrentIndex(self.sourceLangCombo.findData('auto'))
#         self.destLangCombo.setCurrentIndex(self.destLangCombo.findData('en'))
#         self.inputText = QTextEdit()
#         self.outputText = QTextEdit()
#         translate_btn = QPushButton('Translate', self)
#         translate_btn.clicked.connect(self.handleTranslate)
#         layout.addWidget(QLabel("Input Text for Translation:"))
#         layout.addWidget(self.inputText)
#         layout.addWidget(QLabel("Source Language:"))
#         layout.addWidget(self.sourceLangCombo)
#         layout.addWidget(QLabel("Target Language:"))
#         layout.addWidget(self.destLangCombo)
#         layout.addWidget(translate_btn)
#         layout.addWidget(QLabel("Translated Text:"))
#         layout.addWidget(self.outputText)

#     def handleTranslate(self):
#         text = self.inputText.toPlainText().strip()
#         src_lang = self.sourceLangCombo.currentData()
#         dest_lang = self.destLangCombo.currentData()
#         translated = translator.translate(text, src=src_lang, dest=dest_lang)
#         self.outputText.setPlainText(translated.text)

# class LangDetectWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         layout = QVBoxLayout(self)
#         self.text_edit = QTextEdit()
#         detect_btn = QPushButton('Detect', self)
#         detect_btn.clicked.connect(self.detect_language)
#         layout.addWidget(QLabel("Input Text:"))
#         layout.addWidget(self.text_edit)
#         layout.addWidget(detect_btn)

#     def detect_language(self):
#         text = self.text_edit.toPlainText()
#         language = predict(text)
#         QMessageBox.information(self, "Language Detection", f'The text is in {language} language')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = LanguageTranslationSystem()
#     main_window.show()
#     sys.exit(app.exec_())
