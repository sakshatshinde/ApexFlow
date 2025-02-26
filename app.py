import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ai import Gemini

from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setCentralWidget(self.tabWidget)
        self.gemini = Gemini()  # Initialize the Gemini instance
        self.pushButton.clicked.connect(self.handle_send_button)  # Connect the button click to a handler
        self.show()

    def handle_send_button(self):
        prompt: str = self.textEdit.toPlainText()  # Get the text from the `textEdit` box
        self.textBrowser.clear()  # Clear the textBrowser for the new response
        self.textEdit.clear()  # Clear the textEdit field

        if prompt == "":
            return

        response_stream = self.gemini.generate(prompt)  # Generate a response stream using Gemini
        for chunk in response_stream:  # Stream each response chunk
            self.textBrowser.insertPlainText(chunk)  # Append the chunk to the textBrowser
            self.textBrowser.verticalScrollBar().setValue(
                self.textBrowser.verticalScrollBar().maximum()
            )  # Auto-scroll to the bottom
            QApplication.processEvents()  # Allow UI updates during the streaming process

        try:
            self.textBrowser.setMarkdown(self.textBrowser.toPlainText())  # Render as Markdown if possible
        except RuntimeError:
            pass  # Leave the plain text as-is if Markdown rendering fails


app = QApplication(sys.argv)

window = MainWindow()

app.exec()