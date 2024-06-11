import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Simple PyQt5 App")
        self.setGeometry(100, 100, 300, 200)

        # Set up the layout
        layout = QVBoxLayout()

        # Create a label
        self.label = QLabel("Hello, PyQt5!", self)
        layout.addWidget(self.label)

        # Create a button
        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        # Set the layout for the window
        self.setLayout(layout)

    def on_button_click(self):
        self.label.setText("Button Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec_())
