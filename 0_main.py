from PySide6.QtWidgets import *         # Import the PySide6 module
import sys                              # Import the sys module to get the command line arguments

app = QApplication(sys.argv)            # Create a new instance of QApplication
window = QMainWindow()                  # Create a new instance of a window
window.setWindowTitle("First App!")     # Set the window title

button = QPushButton("Click me!")       # Create a button with the text "Click me!"
window.setCentralWidget(button)         # Set the central widget of the window to the button
window.show()                           # Make the window visible

app.exec()                              # Start the event loop