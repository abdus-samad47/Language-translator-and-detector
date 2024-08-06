import sys
from PyQt5.QtWidgets import QApplication
from language_translation_system import LanguageTranslationSystem

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = LanguageTranslationSystem()
    main_window.show()
    sys.exit(app.exec_())
