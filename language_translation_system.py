from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from translate_window import TranslateWindow
from lang_detect_window import LangDetectWindow

class LanguageTranslationSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        detect_btn = QPushButton('Detect Language', self)
        detect_btn.clicked.connect(self.open_lang_detect_window)
        translate_btn = QPushButton('Translate Text', self)
        translate_btn.clicked.connect(self.open_translate_window)
        exit_btn = QPushButton('Exit', self)
        exit_btn.clicked.connect(self.close)
        layout.addWidget(detect_btn)
        layout.addWidget(translate_btn)
        layout.addWidget(exit_btn)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def open_translate_window(self):
        self.translate_window = TranslateWindow()
        self.translate_window.show()

    def open_lang_detect_window(self):
        self.lang_detect_window = LangDetectWindow()
        self.lang_detect_window.show()
