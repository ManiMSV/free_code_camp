from PySide6.QtWidgets import *     # Import the PySide6 module
import sys                        # Import the sys module to get the command line arguments

app = QApplication(sys.argv)    # Create a new instance of QApplication
window = QWidget()           # Create a new instance of a window
window.show()             # Make the window visible

app.exec()              # Start the event loop