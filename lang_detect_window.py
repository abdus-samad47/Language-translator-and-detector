import re
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox
from language_model import predict

class LangDetectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.text_edit = QTextEdit()
        detect_btn = QPushButton('Detect', self)
        detect_btn.clicked.connect(self.detect_language)
        layout.addWidget(QLabel("Input Text:"))
        layout.addWidget(self.text_edit)
        layout.addWidget(detect_btn)
        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 300)

    def detect_language(self):
        text = self.text_edit.toPlainText()
        language = predict(text)
        QMessageBox.information(self, "Language Detection", f'The text is in {language} language')
