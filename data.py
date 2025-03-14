from dataclasses import dataclass

import nsepython as nsepy
from PySide6.QtCore import Signal, QThread
from PySide6.QtWebEngineCore import QWebEngineSettings
import yfinance as yf


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
    indiaVix: str = 0

    # Percent Changes from last value
    nifty50Change: str = 0
    niftyNext50Change: str = 0
    nifty100Change: str = 0
    niftyBankChange: str = 0
    niftyAutoChange: str = 0
    niftyPharmaChange: str = 0
    niftyOilAndGasChange: str = 0
    niftyEnergyChange: str = 0
    niftyMidcap150Change: str = 0
    niftyFmcgChange: str = 0
    niftySmallCap250Change: str = 0
    niftyIndiaDefenceChange: str = 0
    niftyITChange: str = 0
    indiaVixChange: str = 0


# This might seem like a bloated function doing the same things over and over
# But keeping every response seperate makes its maintainable
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
        resIndiaVix = nsepy.nse_get_index_quote("INDIA VIX")

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        raise

    try:
        try:
            nifty50 = resNifty50["last"].replace(',', '')
            nifty50Change = resNifty50["percChange"]
        except Exception as e:
            print(f"Error fetching Nifty50 data: {e}")
            print(f"Response: {resNifty50}")
            nifty50 = 0
            nifty50Change = 0

        try:
            niftyNext50 = resNiftyNext50["last"].replace(',', '')
            niftyNext50Change = resNiftyNext50["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyNext50 data: {e}")
            niftyNext50 = 0
            niftyNext50Change = 0

        try:
            nifty100 = resNifty100["last"].replace(',', '')
            nifty100Change = resNifty100["percChange"]
        except Exception as e:
            print(f"Error fetching Nifty100 data: {e}")
            nifty100 = 0
            nifty100Change = 0

        try:
            niftyBank = resNiftyBank["last"].replace(',', '')
            niftyBankChange = resNiftyBank["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyBank data: {e}")
            niftyBank = 0
            niftyBankChange = 0

        try:
            niftyAuto = resNiftyAuto["last"].replace(',', '')
            niftyAutoChange = resNiftyAuto["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyAuto data: {e}")
            niftyAuto = 0
            niftyAutoChange = 0

        try:
            niftyPharma = resNiftyPharma["last"].replace(',', '')
            niftyPharmaChange = resNiftyPharma["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyPharma data: {e}")
            niftyPharma = 0
            niftyPharmaChange = 0

        try:
            niftyOilAndGas = resNiftyOilAndGas["last"].replace(',', '')
            niftyOilAndGasChange = resNiftyOilAndGas["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyOilAndGas data: {e}")
            niftyOilAndGas = 0
            niftyOilAndGasChange = 0

        try:
            niftyEnergy = resNiftyEnergy["last"].replace(',', '')
            niftyEnergyChange = resNiftyEnergy["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyEnergy data: {e}")
            niftyEnergy = 0
            niftyEnergyChange = 0

        try:
            niftySmallCap250 = resNiftySmallCap250["last"].replace(',', '')
            niftySmallCap250Change = resNiftySmallCap250["percChange"]
        except Exception as e:
            print(f"Error fetching NiftySmallCap250 data: {e}")
            niftySmallCap250 = 0
            niftySmallCap250Change = 0
        try:
            niftyMidcap150 = resNiftyMidcap150["last"].replace(',', '')
            niftyMidcap150Change = resNiftyMidcap150["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyMidcap150 data: {e}")
            niftyMidcap150 = 0
            niftyMidcap150Change = 0
        try:
            niftyIndiaDefence = resNiftyIndiaDefence["last"].replace(',', '')
            niftyIndiaDefenceChange = resNiftyIndiaDefence["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyIndiaDefence data: {e}")
            niftyIndiaDefence = 0
            niftyIndiaDefenceChange = 0
        try:
            niftyFmcg = resNiftyFmcg["last"].replace(',', '')
            niftyFmcgChange = resNiftyFmcg["percChange"]
        except Exception as e:
            print(f"Error fetching NiftyFmcg data: {e}")
            niftyFmcg = 0
            niftyFmcgChange = 0

        try:
            niftyIT = resNiftyIT["last"].replace(',', '')
            niftyITChange = resNiftyIT["percChange"]
        except Exception as e:
            print(f"Error fetching niftyIT data: {e}")
            niftyIT = 0
            niftyITChange = 0

        try:
            indiaVix = resIndiaVix["last"].replace(',', '')
            indiaVixChange = resIndiaVix["percChange"]
        except Exception as e:
            print(f"Error fetching India VIX data: {e}")
            indiaVix = 0
            indiaVixChange = 0

        return IndiaStockIndices(
            nifty50=nifty50,
            nifty50Change=nifty50Change,
            niftyNext50=niftyNext50,
            niftyNext50Change=niftyNext50Change,
            nifty100=nifty100,
            nifty100Change=nifty100Change,
            niftyBank=niftyBank,
            niftyBankChange=niftyBankChange,
            niftyAuto=niftyAuto,
            niftyAutoChange=niftyAutoChange,
            niftyPharma=niftyPharma,
            niftyPharmaChange=niftyPharmaChange,
            niftyOilAndGas=niftyOilAndGas,
            niftyOilAndGasChange=niftyOilAndGasChange,
            niftyEnergy=niftyEnergy,
            niftyEnergyChange=niftyEnergyChange,
            niftySmallCap250=niftySmallCap250,
            niftySmallCap250Change=niftySmallCap250Change,
            niftyMidcap150=niftyMidcap150,
            niftyMidcap150Change=niftyMidcap150Change,
            niftyIndiaDefence=niftyIndiaDefence,
            niftyIndiaDefenceChange=niftyIndiaDefenceChange,
            niftyFmcg=niftyFmcg,
            niftyFmcgChange=niftyFmcgChange,
            niftyIT=niftyIT,
            niftyITChange=niftyITChange,
            indiaVix=indiaVix,
            indiaVixChange=indiaVixChange
        )
    except Exception as e:
        print(f"Error creating IndiaStockIndices object: {e}")
        raise


@dataclass
class OtherStockIndices:
    msciWorld: str = 0
    nasdaq100: str = 0
    sp500: str = 0
    nikkei225: str = 0
    hangSeng: str = 0

    msciWorldChange: str = 0
    nasdaq100Change: str = 0
    sp500Change: str = 0
    nikkei225Change: str = 0
    hangSengChange: str = 0


def refreshOtherStockIndices() -> OtherStockIndices:
    try:
        resmsciWorld = yf.Ticker("^990100-GBP-NETR")
        resnasdaq100 = yf.Ticker("^NDX")
        resp500 = yf.Ticker("^GSPC")
        resnikkei225 = yf.Ticker("^N225")
        reshangSeng = yf.Ticker("^HSI")

        return OtherStockIndices(
            msciWorld=resmsciWorld.info['regularMarketPrice'],
            nasdaq100=resnasdaq100.info['regularMarketPrice'],
            sp500=resp500.info['regularMarketPrice'],
            nikkei225=resnikkei225.info['regularMarketPrice'],
            hangSeng=reshangSeng.info['regularMarketPrice'],
            msciWorldChange=resmsciWorld.info['regularMarketChangePercent'],
            nasdaq100Change=resnasdaq100.info['regularMarketChangePercent'],
            sp500Change=resp500.info['regularMarketChangePercent'],
            nikkei225Change=resnikkei225.info['regularMarketChangePercent'],
            hangSengChange=reshangSeng.info['regularMarketChangePercent'],
        )

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        raise


@dataclass
class Commodities:
    gold: str = 0
    silver: str = 0
    brentCrudeOil: str = 0
    naturalGas: str = 0

    goldChange: str = 0
    silverChange: str = 0
    brentCrudeOilChange: str = 0
    naturalGasChange: str = 0


@dataclass
class Forex:
    PairUsdInr: str = 0
    usVix: str = 0
    PairUsdInrChange: str = 0
    usVixChange: str = 0


@dataclass
class IndicesTabData:
    india: IndiaStockIndices
    other: OtherStockIndices
    commodities: Commodities
    forex: Forex


def refreshCommodities() -> Commodities:
    try:
        resGold = yf.Ticker("GC=F")
        resSilver = yf.Ticker("SI=F")
        resBrentCrudeOil = yf.Ticker("BZ=F")
        resNaturalGas = yf.Ticker("NG=F")
    except Exception as e:
        print(f"Error fetching commodities data: {e}")
        raise

    return Commodities(
        gold=resGold.info['regularMarketPrice'],
        silver=resSilver.info['regularMarketPrice'],
        brentCrudeOil=resBrentCrudeOil.info['regularMarketPrice'],
        naturalGas=resNaturalGas.info['regularMarketPrice'],
        goldChange=resGold.info['regularMarketChangePercent'],
        silverChange=resSilver.info['regularMarketChangePercent'],
        brentCrudeOilChange=resBrentCrudeOil.info['regularMarketChangePercent'],
        naturalGasChange=resNaturalGas.info['regularMarketChangePercent'],
    )


def refreshForex() -> Forex:
    try:
        resUsdInr = yf.Ticker("INR=X")
        resUsVix = yf.Ticker("^VIX")

        return Forex(
            PairUsdInr=resUsdInr.info['regularMarketPrice'],
            PairUsdInrChange=resUsdInr.info['regularMarketChangePercent'],
            usVix=resUsVix.info['regularMarketPrice'],
            usVixChange=resUsVix.info['regularMarketChangePercent'],
        )

    except Exception as e:
        print(f"Error fetching forex data: {e}")
        raise


# Worker class to fetch data and send it as a signal to QT
class StockDataWorker(QThread):
    dataReady = Signal(IndicesTabData)

    def run(self):
        try:
            indiaData = refreshIndiaStockIndices()
            otherData = refreshOtherStockIndices()
            commoditiesData = refreshCommodities()
            forexData = refreshForex()

            data = IndicesTabData(india=indiaData, other=otherData, commodities=commoditiesData, forex=forexData)
            self.dataReady.emit(data)

        except Exception as e:
            print(f"Error in StockDataWorker: {e}")


def wvSettings(wv) -> QWebEngineSettings:
    settings = wv.settings()
    settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.ScrollAnimatorEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)

    return settings


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

    _settings = wvSettings(wv)
    wv.setHtml(html_content)


def setupSectoralWebViewTwo(wv):
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
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
  {
  "feedMode": "all_symbols",
  "isTransparent": false,
  "displayMode": "regular",
  "width": "100%",
  "height": "100%",
  "colorTheme": "dark",
  "locale": "en"
}
  </script>
</div>
<!-- TradingView Widget END -->
    
    '''

    _settings = wvSettings(wv)
    wv.setHtml(html_content)


def setupSectoralWebViewOne(wv):
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
  <div class="tradingview-widget-copyright">ApexFlow Sectoral Overview</a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-quotes.js" async>
  {
  "width": "100%",
  "height": "100%",
  "symbolsGroups": [
    {
      "name": "Sector Indices",
      "symbols": [
        {
          "name": "BSE:IT",
          "displayName": "BSE IT"
        },
        {
          "name": "BSE:IPO",
          "displayName": "BSE IPO"
        },
        {
          "name": "BSE:BSEPBI",
          "displayName": "BSE Private Banks"
        },
        {
          "name": "BSE:PSU",
          "displayName": "BSE PSU"
        },
        {
          "name": "BSE:FMCG",
          "displayName": "BSE FMCG"
        },
        {
          "name": "BSE:INFRASTRUCTURE",
          "displayName": "BSE Infra"
        },
        {
          "name": "BSE:HC",
          "displayName": "BSE Healthcare"
        },
        {
          "name": "BSE:REALTY",
          "displayName": "BSE Realty"
        },
        {
          "name": "BSE:PRECON",
          "displayName": "BSE Premium Consumption"
        },
        {
          "name": "BSE:POWENE",
          "displayName": "BSE Power & Energy"
        },
        {
          "name": "BSE:OILGAS",
          "displayName": "BSE Oil & Gas"
        },
        {
          "name": "BSE:METAL",
          "displayName": "BSE Metals"
        },
        {
          "name": "BSE:MFG",
          "displayName": "BSE Manufacturing"
        }
      ]
    },
    {
      "name": "Metals",
      "symbols": [
        {
          "name": "TVC:GOLD",
          "displayName": "Gold"
        },
        {
          "name": "TVC:SILVER",
          "displayName": "Silver"
        }
      ]
    },
    {
      "name": "Major Indices",
      "symbols": [
        {
          "name": "BSE:SENSEX",
          "displayName": "Sensex"
        },
        {
          "name": "BSE:BSEMOI",
          "displayName": "BSE Momentum"
        },
        {
          "name": "BSE:SMLCAP",
          "displayName": "BSE Smallcap"
        },
        {
          "name": "BSE:MIDCAP",
          "displayName": "BSE Midcap"
        }
      ]
    }
  ],
  "showSymbolLogo": true,
  "isTransparent": false,
  "colorTheme": "dark",
  "locale": "en",
  "backgroundColor": "#131722"
}
  </script>
</div>
<!-- TradingView Widget END -->
'''

    _settings = wvSettings(wv)

    wv.setHtml(html_content)


def setupSectoralWebViewThree(wv):
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
<div class="tradingview-widget-container" style="height:100%;width:100%">
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
  {
  "autosize": true,
  "symbol": "BSE:SENSEX",
  "interval": "D",
  "timezone": "Asia/Kolkata",
  "theme": "dark",
  "style": "3",
  "locale": "en",
  "allow_symbol_change": true,
  "compareSymbols": [
    {
      "symbol": "NASDAQ:NDX",
      "position": "SameScale"
    },
    {
      "symbol": "FRED:SP500",
      "position": "SameScale"
    },
    {
      "symbol": "HSI:HSI",
      "position": "SameScale"
    },
    {
      "symbol": "ICMARKETS:JP225",
      "position": "SameScale"
    }
  ],
  "details": true,
  "calendar": false,
  "support_host": "https://www.tradingview.com"
}
  </script>
</div>
<!-- TradingView Widget END -->
'''

    _settings = wvSettings(wv)
    wv.setHtml(html_content)


def setupSectoralWebViewFour(wv):
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
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
  {
  "symbols": [
    [
      "BSE:SMLCAP|3M"
    ],
    [
      "BSE:MIDCAP|3M"
    ],
    [
      "BSE:IT|3M"
    ],
    [
      "Banks",
      "BSE:BSEPBI|1D"
    ]
  ],
  "chartOnly": false,
  "width": "100%",
  "height": "100%",
  "locale": "en",
  "colorTheme": "dark",
  "autosize": true,
  "showVolume": true,
  "showMA": false,
  "hideDateRanges": false,
  "hideMarketStatus": false,
  "hideSymbolLogo": false,
  "scalePosition": "right",
  "scaleMode": "Normal",
  "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
  "fontSize": "10",
  "noTimeScale": false,
  "valuesTracking": "1",
  "changeMode": "price-and-percent",
  "chartType": "area",
  "headerFontSize": "medium",
  "lineWidth": 2,
  "lineType": 0,
  "dateRanges": [
    "1d|1",
    "1m|30",
    "3m|60",
    "12m|1D",
    "60m|1W",
    "all|1M"
  ]
}
  </script>
</div>
<!-- TradingView Widget END -->

    '''

    _settings = wvSettings(wv)
    wv.setHtml(html_content)


def aboutTabWebView(wv):
    html_content = '''
    <!DOCTYPE html>
<html>
<head>
<style>
  body {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    margin: 0;
    padding: 0;
    background-color: #1f2937;
    color: #a3e635;
    line-height: 1.4;
  }
  
  .about-window {
    padding: 20px;
    max-width: 500px;
    margin: 0 auto;
  }
  
  .app-header {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .app-name {
    font-size: 28px;
    font-weight: bold;
    margin: 0;
    margin-bottom: 4px;
    color: #4f46e5;
    text-shadow: 0 0 8px rgba(79, 70, 229, 0.6);
  }
  
  .app-version {
    font-size: 13px;
    color: #818cf8;
    margin: 0;
  }
  
  .divider {
    height: 1px;
    background: linear-gradient(to right, transparent, #4f46e5, transparent);
    margin: 15px 0;
    position: relative;
  }
  
  .divider::after {
    content: "<EOF>";
    position: absolute;
    top: -8px;
    right: 0;
    background: #1f2937;
    padding: 0 5px;
    font-size: 12px;
    color: #9ca3af;
  }
  
  .section-title {
    font-weight: bold;
    color: #4f46e5;
    margin-bottom: 8px;
  }
  
  .section-title::before {
    content: ">> ";
    color: #818cf8;
  }
  
  .info-section {
    margin-bottom: 15px;
  }
  
  .info-row {
    display: flex;
    margin-bottom: 4px;
  }
  
  .info-label {
    flex: 0 0 100px;
    color: #818cf8;
  }
  
  .info-label::after {
    content: ":";
  }
  
  .info-value {
    flex: 1;
  }
  
  a {
    color: #60a5fa;
    text-decoration: none;
    border-bottom: 1px dashed #60a5fa;
    padding-bottom: 1px;
  }
  
  a:hover {
    color: #93c5fd;
    border-bottom-style: solid;
  }
  
  .copyright {
    font-size: 12px;
    color: #9ca3af;
    margin-top: 20px;
    text-align: center;
  }
  
  .ascii-table {
    font-family: monospace;
    white-space: pre;
    font-size: 12px;
    line-height: 1.2;
    color: #818cf8;
    margin-top: 10px;
  }
  
  .ascii-table a {
    border-bottom: none;
  }
  
  .repository-link {
    margin-bottom: 10px;
  }
</style>
</head>
<body>

<div class="about-window">
  <div class="app-header">
    <h1 class="app-name">ApexFlow</h1>
    <p class="app-version">v1.0.0-stable</p>
  </div>
  
  <div class="divider"></div>
  
  <div class="info-section">
    <div class="section-title">System Info</div>
    <div class="info-row">
      <div class="info-label">Developer</div>
      <div class="info-value">Sakshat Shinde</div>
    </div>
    <div class="info-row">
      <div class="info-label">License</div>
      <div class="info-value">GPLv3</div>
    </div>
    <div class="info-row">
      <div class="info-label">Build</div>
      <div class="info-value">20250314.1</div>
    </div>
  </div>
  
  <div class="divider"></div>
  
  <div class="info-section">
        <div class="section-title">Software used</div>
        <div class="info-row">
          <div class="info-label">Python</div>
          <div class="info-value">3.12</div>
        </div>
        <div class="info-row">
          <div class="info-label">QT</div>
          <div class="info-value">PySide6 6.8.2.1</div>
        </div>
        <div class="info-row">
          <div class="info-label">nsepython</div>
          <div class="info-value">2.94</div>
        </div>
        <div class="info-row">
          <div class="info-label">yfinance</div>
          <div class="info-value">0.2.54</div>
        </div>
  </div>
    
<div class="divider"></div>
    
  <div class="info-section">
    <div class="section-title">Support Vector</div>
    <div class="ascii-table">
╔══════════════════════════════════════════════════════════════╗
║                      DONATION CHANNELS                       ║
╠═══════════════╦══════════════════════════════════════════════╣
║ Metamask      ║ 0x3448729cdF18051727A8d2fFe5A5322F433e1D09   ║
╠═══════════════╬══════════════════════════════════════════════╣
║ UPI           ║ sakshatshinde@pingpay                        ║
╚═══════════════╩══════════════════════════════════════════════╝
    </div>
  </div>
  
  <div class="divider"></div>
  
  <div class="copyright">
    © 2025 Sakshat Shinde. All rights reserved.
  </div>
</div>

</body>
</html>
    '''

    wv.setHtml(html_content)

    settings = wv.settings()

    settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, False)
    settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)
