import sys
from PySide6.QtWidgets import *

class button_holder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First App! - Button Holder")
        button = QPushButton("Click me!")

        self.setCentralWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = button_holder()
    window.show()
    app.exec()



        