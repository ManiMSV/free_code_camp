import sys
from PySide6.QtWidgets import *
from button_holder import button_holder

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = button_holder()
    window.show()
    app.exec()



        