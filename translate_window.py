from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox
from googletrans import Translator, LANGUAGES

# Global Translator initialization
translator = Translator()

class TranslateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.sourceLangCombo = QComboBox()
        self.destLangCombo = QComboBox()
        for lang_code, lang_name in sorted(LANGUAGES.items(), key=lambda x: x[1]):
            self.sourceLangCombo.addItem(lang_name, lang_code)
            self.destLangCombo.addItem(lang_name, lang_code)
        self.sourceLangCombo.setCurrentIndex(self.sourceLangCombo.findData('auto'))
        self.destLangCombo.setCurrentIndex(self.destLangCombo.findData('en'))
        self.inputText = QTextEdit()
        self.outputText = QTextEdit()
        translate_btn = QPushButton('Translate', self)
        translate_btn.clicked.connect(self.handleTranslate)
        layout.addWidget(QLabel("Input Text for Translation:"))
        layout.addWidget(self.inputText)
        layout.addWidget(QLabel("Source Language:"))
        layout.addWidget(self.sourceLangCombo)
        layout.addWidget(QLabel("Target Language:"))
        layout.addWidget(self.destLangCombo)
        layout.addWidget(translate_btn)
        layout.addWidget(QLabel("Translated Text:"))
        layout.addWidget(self.outputText)
        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 300)

    def handleTranslate(self):
        text = self.inputText.toPlainText().strip()
        src_lang = self.sourceLangCombo.currentData()
        dest_lang = self.destLangCombo.currentData()
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        self.outputText.setPlainText(translated.text)
