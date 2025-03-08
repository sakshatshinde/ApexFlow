from dataclasses import dataclass

import nsepython as nsepy
from PySide6.QtCore import Signal, QThread
from PySide6.QtWebEngineCore import QWebEngineSettings


@dataclass
class IndiaStockIndices:
    nifty50: str = 0
    niftyNext50: str = 0
    nifty100: str = 0
    niftyBank: str = 0
    niftyAuto: str = 0
    niftyPharma: str = 0
    niftyOilAndGas: str = 0
    niftyEnergy: str = 0
    niftyMidcap150: str = 0
    niftyFmcg: str = 0
    niftySmallCap250: str = 0
    niftyIndiaDefence: str = 0
    niftyIT: str = 0


def refreshIndiaStockIndices() -> IndiaStockIndices:
    # Available indexes
    # ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY IT', 'NIFTY BANK', 'INDIA VIX', 'NIFTY 100', 'NIFTY 500', 'NIFTY MIDCAP 100',
    #  'NIFTY MIDCAP 50', 'NIFTY INFRA', 'NIFTY REALTY', 'BHARATBOND-APR3
    #  0', 'NIFTY FMCG', 'NIFTY GS 8 13YR', 'NIFTY IND DIGITAL', 'NIFTY MICROCAP250', 'NIFTY MOBILITY', 'NIFTY MS IT TELCM
    #  ', 'NIFTY NEW CONSUMP', 'NIFTY PSE', 'NIFTY TRANS LOGIS', 'NIFTY10
    #  0 LOWVOL30', 'NIFTY200 VALUE 30', 'NIFTY50 VALUE 20', 'NIFTY500 EW', 'NIFTY ALPHALOWVOL', 'NIFTY ENERGY', 'NIFTY
    #  IND TOURISM', 'NIFTY M150 QLTY50', 'NIFTY MIDCAP 150', 'NIFTY MS FIN SERV', 'NIFTY NONCYC CONS', 'NIFTY PSU BANK
    #  ', 'NIFTY SML250 Q50', 'NIFTY SMALLCAP 250', 'NIFTY TOP 10 EW', 'NIFTY100 ENH ESG', 'NIFTY50 PR 2X LEV', 'NIFTY50
    #  TR 1X INV', 'NIFTY 200', 'NIFTY AQL 30', 'NIFTY COREHOUSING', 'NIFTY CORP MAATR', 'NIFTY MID LIQ 15', 'NIFTY PVT
    #  BANK', 'NIFTY SERV SECTOR', 'NIFTY SHARIAH 25', 'NIFTY100 ESG', 'NIFTY100 LIQ 15', 'NIFTY100ESGSECLDR', '
    #  NIFTY500MOMENTM50', 'BHARATBOND - APR31', 'NIFTY AUTO', 'NIFTY CONSUMPTION', 'NIFTY EV', 'NIFTY FINSEREXBNK', '
    #  NIFTY GS 10YR CLN', 'NIFTY GS 11 15YR', 'NIFTY GS COMPSITE', 'NIFTY HIGHBETA 50', 'NIFTY IND DEFENCE', 'NIFTY INDIA
    #  MFG', 'NIFTY LOW VOL 50', 'NIFTY METAL', 'NIFTY MS IND CONS', 'NIFTY MULTI INFRA', 'NIFTY MULTI MFG', 'NIFTY QLTY
    #  LV 30', 'NIFTY SMALLCAP 50', 'NIFTY TOP 20 EW', 'NIFTY200 ALPHA 30', 'NIFTY50 TR 2X LEV', 'NIFTY500 VALUE 50', '
    #  BHARATBOND - APR33', 'NIFTY ALPHA 50', 'NIFTY AQLV 30', 'NIFTY COMMODITIES', 'NIFTY DIV OPPS 50', 'NIFTY FINSRV25
    #  50', 'NIFTY GROWSECT 15', 'NIFTY HEALTHCARE', 'NIFTY MID SELECT', 'NIFTY OIL AND GAS', 'NIFTY500 SHARIAH', '
    #  NIFTYMS400 MQ 100', 'BHARATBOND - APR32', 'INDEX1 NSETEST', 'INDEX2 NSETEST', 'NIFTY CAPITAL MKT', 'NIFTY GS 10YR
    #  ', 'NIFTY GS 15YRPLUS', 'NIFTY MEDIA', 'NIFTY MULTI MQ 50', 'NIFTY RURAL', 'NIFTY100 ALPHA 30', 'NIFTY50 DIV POINT
    #  ', 'BHARATBOND - APR25', 'NIFTY CONSR DURBL', 'NIFTY CPSE', 'NIFTY FIN SERVICE', 'NIFTY GS 4 8YR', 'NIFTY IPO', '
    #  NIFTY MIDSMALLCAP 400', 'NIFTY MIDSML HLTH', 'NIFTY MNC', 'NIFTY SMLCAP 100', 'NIFTY INDIA CORPORATE GROUP
    #  INDEX - TATA GROUP 25 CAP', 'NIFTY TOP 15 EW', 'NIFTY200 QUALTY30', 'NIFTY50 PR 1X INV', 'NIFTY500 LMS EQL', '
    #  NIFTYSML250MQ 100', 'NIFTY HOUSING', 'NIFTY LARGEMID250', 'NIFTY PHARMA', 'NIFTY TOTAL MKT', 'NIFTY100 EQL WGT', '
    #  NIFTY100 QUALTY30', 'NIFTY200 MOMENTM30', 'NIFTY50 EQL WGT', 'NIFTY50 SHARIAH', 'NIFTY500 MULTICAP', 'Nifty
    #  Midcap150 Momentum 50', 'NIFTY INDIA CORPORATE GROUP INDEX - MAHINDRA GROUP', 'NIFTY INDIA CORPORATE GROUP
    #  INDEX - ADITYA BIRLA GROUP', 'NIFTY INDIA CORPORATE GROUP INDEX - TATA GROUP', 'NIFTY SME EMERGE', 'NIFTY
    #  REITS & INVITS', 'NIFTY INDIA RAILWAYS PSU', 'NIFTY500 MULTIFACTOR MQVLV 50', 'NIFTY500 QUALITY 50', 'NIFTY500 LOW
    #  VOLATILITY 50']
    try:
        resNifty50 = nsepy.nse_get_index_quote("NIFTY 50")
        resNiftyNext50 = nsepy.nse_get_index_quote("NIFTY NEXT 50")
        resNiftyBank = nsepy.nse_get_index_quote("NIFTY BANK")
        resNiftyAuto = nsepy.nse_get_index_quote("NIFTY AUTO")
        resNiftyPharma = nsepy.nse_get_index_quote("NIFTY PHARMA")
        resNiftyOilAndGas = nsepy.nse_get_index_quote("NIFTY OIL AND GAS")
        resNiftyEnergy = nsepy.nse_get_index_quote("NIFTY ENERGY")
        resNiftySmallCap250 = nsepy.nse_get_index_quote("NIFTY SMALLCAP 250")
        resNiftyMidcap150 = nsepy.nse_get_index_quote("NIFTY MIDCAP 150")
        resNiftyIndiaDefence = nsepy.nse_get_index_quote("NIFTY IND DEFENCE")
        resNiftyFmcg = nsepy.nse_get_index_quote("NIFTY FMCG")
        resNifty100 = nsepy.nse_get_index_quote("NIFTY 100")
        resNiftyIT = nsepy.nse_get_index_quote("NIFTY IT")

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        raise

    try:
        try:
            nifty50 = resNifty50["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching Nifty50: {e}")
            nifty50 = 0

        try:
            niftyNext50 = resNiftyNext50["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyNext50: {e}")
            niftyNext50 = 0

        try:
            nifty100 = resNifty100["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching Nifty100: {e}")
            nifty100 = 0

        try:
            niftyBank = resNiftyBank["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyBank: {e}")
            niftyBank = 0

        try:
            niftyAuto = resNiftyAuto["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyAuto: {e}")
            niftyAuto = 0

        try:
            niftyPharma = resNiftyPharma["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyPharma: {e}")
            niftyPharma = 0

        try:
            niftyOilAndGas = resNiftyOilAndGas["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyOilAndGas: {e}")
            niftyOilAndGas = 0

        try:
            niftyEnergy = resNiftyEnergy["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyEnergy: {e}")
            niftyEnergy = 0

        try:
            niftySmallCap250 = resNiftySmallCap250["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftySmallCap250: {e}")
            niftySmallCap250 = 0

        try:
            niftyMidcap150 = resNiftyMidcap150["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyMidcap150: {e}")
            niftyMidcap150 = 0

        try:
            niftyIndiaDefence = resNiftyIndiaDefence["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyIndiaDefence: {e}")
            niftyIndiaDefence = 0

        try:
            niftyFmcg = resNiftyFmcg["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching NiftyFmcg: {e}")
            niftyFmcg = 0

        try:
            niftyIT = resNiftyIT["last"].replace(',', '')
        except Exception as e:
            print(f"Error fetching niftyIT: {e}")
            resNiftyIT = 0

        return IndiaStockIndices(
            nifty50=nifty50,
            niftyNext50=niftyNext50,
            nifty100=nifty100,
            niftyBank=niftyBank,
            niftyAuto=niftyAuto,
            niftyPharma=niftyPharma,
            niftyOilAndGas=niftyOilAndGas,
            niftyEnergy=niftyEnergy,
            niftySmallCap250=niftySmallCap250,
            niftyMidcap150=niftyMidcap150,
            niftyIndiaDefence=niftyIndiaDefence,
            niftyFmcg=niftyFmcg,
            niftyIT=niftyIT,
        )
    except Exception as e:
        print(f"Error creating IndiaStockIndices object: {e}")
        raise


# Worker class to fetch data and send it as a signal to QT
class StockDataWorker(QThread):
    dataReady = Signal(IndiaStockIndices)

    def run(self):
        try:
            data = refreshIndiaStockIndices()
            self.dataReady.emit(data)
        except Exception as e:
            print(f"Error in StockDataWorker: {e}")


def setupNiftyHeatmap(wv):
    """
    Sets up the QWebEngineView with the Nifty 50 PE ratio chart.

    Args:
        webview: QWebEngineView instance to display the chart
    """
    html_content = '''
     <style>
            body {
                background-color: #2b2b2b;  /* Dark background */
                color: #ffffff;             /* Light text */
                margin: 0;
                padding: 0;
            }
        </style>

    <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright">ApexFlow Indian Markets HeatMap - Powered by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>
  {
  "exchanges": [],
  "dataSource": "SENSEX",
  "grouping": "sector",
  "blockSize": "market_cap_basic",
  "blockColor": "change",
  "locale": "en",
  "symbolUrl": "",
  "colorTheme": "dark",
  "hasTopBar": false,
  "isDataSetEnabled": false,
  "isZoomEnabled": true,
  "hasSymbolTooltip": true,
  "isMonoSize": false,
  "width": "100%",
  "height": "100%"
}
  </script>
</div>


<!-- TradingView Widget END -->
'''

    settings = wv.settings()

    # settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
    # settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
    # settings.setAttribute(QWebEngineSettings.WebAttribute.AllowWindowActivationFromJavaScript, True)

    settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.ScrollAnimatorEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)

    wv.setHtml(html_content)
