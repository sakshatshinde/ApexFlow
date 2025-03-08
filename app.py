import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon

from ai import Gemini
from data import StockDataWorker, IndiaStockIndices, setupNiftyHeatmap

from ui.ui_main import Ui_MainWindow


def getPercentageStyle(change_value):
    """Generate stylesheet for percentage labels based on the change value."""
    try:
        change = float(change_value)

        # Common style properties
        base_style = """
            font-family: 'Segoe UI', Arial;
            font-size: 16px;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 4px;
            margin: 2px;
        """

        if change < 0:
            # Red theme for negative values
            return {
                "text": f"{change:.2f}%",
                "style": f"""
                    QLabel {{ 
                        {base_style}
                        color: #FF3B30; 
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 rgba(255, 59, 48, 0.2), 
                                    stop:1 rgba(255, 59, 48, 0.1));
                        border: 1px solid rgba(255, 59, 48, 0.3);
                    }}
                """,
                "lcd_style": "QLCDNumber { color: red; }"
            }
        else:
            # Green theme for positive values
            return {
                "text": f"+{change:.2f}%",
                "style": f"""
                    QLabel {{ 
                        {base_style}
                        color: #34C759; 
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 rgba(52, 199, 89, 0.2), 
                                    stop:1 rgba(52, 199, 89, 0.1));
                        border: 1px solid rgba(52, 199, 89, 0.3);
                    }}
                """,
                "lcd_style": "QLCDNumber { color: #34C759; }"
            }

    except (ValueError, TypeError):
        # Handle cases where change_value isn't a valid float
        return {
            "text": "N/A",
            "style": f"""
                QLabel {{ 
                    {base_style}
                    color: #CCCCCC;
                    background-color: rgba(150, 150, 150, 0.2);
                    border: 1px solid rgba(150, 150, 150, 0.3);
                }}
            """,
            "lcd_style": "QLCDNumber { color: white; }"
        }


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setCentralWidget(self.tabWidget)
        self.setWindowIcon(QIcon("ui/apexFlowIcon.png"))

        self.gemini = Gemini()  # Initialize the Gemini instance
        self.send_msg_to_ai_btn.clicked.connect(self.handle_send_button)  # Connect the button click to a handler
        self.clear_prompt_btn.clicked.connect(self.handle_ai_prompt_cler_btn)

        # Stock watcher worker
        self.stockWorker = StockDataWorker()
        self.stockWorker.dataReady.connect(self.update_stock_displays)

        # Timer for the stock watcher
        self.updateTimer = QTimer()
        self.updateTimer.timeout.connect(self.refreshStockData)
        self.updateTimer.setInterval(60000)
        self.updateTimer.start()

        self.refreshStockData()  # Init - runs only once rest is fired by timer above

        # Insert data into heatmap
        setupNiftyHeatmap(self.NiftyHeatmapWebView)

        self.show()

    def refreshStockData(self):
        self.stockWorker.start()

    def update_display_with_percentage(self, lcd_display, percentage_label, value, change_value):
        # Update the LCD display (without changing its style)
        lcd_display.display(value)

        # Get styling from the helper function
        styleInfo = getPercentageStyle(change_value)

        lcd_display.setStyleSheet(styleInfo["lcd_style"])

        # If percentage label exists, update it with enhanced styling
        if hasattr(self, percentage_label):
            percentage_obj = getattr(self, percentage_label)
            # Apply styling
            percentage_obj.setText(styleInfo["text"])
            percentage_obj.setStyleSheet(styleInfo["style"])

    def update_stock_displays(self, data: IndiaStockIndices):
        self.Nifty50.display(data.nifty50)
        # self.NiftyNext50.display(data.niftyNext50)
        # self.Nifty100.display(data.nifty100)
        self.NiftyBank.display(data.niftyBank)
        self.NiftyAuto.display(data.niftyAuto)
        self.NiftyPharma.display(data.niftyPharma)
        self.NiftyOilGas.display(data.niftyOilAndGas)
        self.NiftyEnergy.display(data.niftyEnergy)
        self.NiftySmallCap250.display(data.niftySmallCap250)
        self.NiftyMidcap150.display(data.niftyMidcap150)
        self.NiftyIndiaDefence.display(data.niftyIndiaDefence)
        self.NiftyFMCG.display(data.niftyFmcg)
        self.NiftyIT.display(data.niftyIT)

        # Update each display with its corresponding value and percentage change
        self.update_display_with_percentage(self.Nifty50, 'Nifty50_Percentage', data.nifty50, data.nifty50Change)
        self.update_display_with_percentage(self.NiftyBank, 'NiftyBank_Percentage', data.niftyBank,
                                            data.niftyBankChange)
        self.update_display_with_percentage(self.NiftyAuto, 'NiftyAuto_Percentage', data.niftyAuto,
                                            data.niftyAutoChange)
        self.update_display_with_percentage(self.NiftyPharma, 'NiftyPharma_Percentage', data.niftyPharma,
                                            data.niftyPharmaChange)
        self.update_display_with_percentage(self.NiftyOilGas, 'NiftyOilGas_Percentage', data.niftyOilAndGas,
                                            data.niftyOilAndGasChange)
        self.update_display_with_percentage(self.NiftyEnergy, 'NiftyEnergy_Percentage', data.niftyEnergy,
                                            data.niftyEnergyChange)
        self.update_display_with_percentage(self.NiftySmallCap250, 'NiftySmallCap250_Percentage', data.niftySmallCap250,
                                            data.niftySmallCap250Change)
        self.update_display_with_percentage(self.NiftyMidcap150, 'NiftyMidcap150_Percentage', data.niftyMidcap150,
                                            data.niftyMidcap150Change)
        self.update_display_with_percentage(self.NiftyIndiaDefence, 'NiftyIndiaDefence_Percentage',
                                            data.niftyIndiaDefence, data.niftyIndiaDefenceChange)
        self.update_display_with_percentage(self.NiftyFMCG, 'NiftyFMCG_Percentage', data.niftyFmcg,
                                            data.niftyFmcgChange)
        self.update_display_with_percentage(self.NiftyIT, 'NiftyIT_Percentage', data.niftyIT, data.niftyITChange)

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


