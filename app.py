import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

from ai import Gemini
from data import StockDataWorker, IndiaStockIndices

from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setCentralWidget(self.tabWidget)
        self.gemini = Gemini()  # Initialize the Gemini instance
        self.send_msg_to_ai_btn.clicked.connect(self.handle_send_button)  # Connect the button click to a handler
        self.clear_prompt_btn.clicked.connect(self.handle_ai_prompt_cler_btn)

        # Stock watcher worker
        self.stockWorker = StockDataWorker()
        self.stockWorker.dataReady.connect(self.updateStockDisplays)

        # Timer for the stock watcher
        self.updateTimer = QTimer()
        self.updateTimer.timeout.connect(self.refreshStockData)
        self.updateTimer.setInterval(60000)
        self.updateTimer.start()

        self.refreshStockData()  # Init - runs only once rest is fired by timer above

        self.show()

    def refreshStockData(self):
        self.stockWorker.start()

    def updateStockDisplays(self, data: IndiaStockIndices):
        self.Nifty50.display(data.nifty50)
        # self.NiftyNext50.display(data.niftyNext50)
        # self.Nifty100.display(data.nifty100)
        self.NiftyBank.display(data.niftyBank)
        self.NiftyAuto.display(data.niftyAuto)
        self.NiftyPharma.display(data.niftyPharma)
        self.NIftyOilGas.display(data.niftyOilAndGas)
        self.NiftyEnergy.display(data.niftyEnergy)
        self.NiftySmallCap250.display(data.niftySmallCap250)
        self.NiftyMidcap150.display(data.niftyMidcap150)
        self.NiftyIndiaDefence.display(data.niftyIndiaDefence)
        self.NiftyFMCG.display(data.niftyFmcg)
        self.NiftyIT.display(data.niftyIT)

    def handle_ai_prompt_cler_btn(self):
        self.textEdit.clear()

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
