import requests
import json

"""
Base URL for
"""
URL_CHART = 'http://thecse.com/mssql/get/CNSX/chart/';

"""
Base URL for depth
"""
URL_DEPTH = 'http://thecse.com/mssql/get/CNSX/dept/';

"""
Base URL for depth price
"""
URL_DEPTH_PRICE = 'http://thecse.com/mssql/get/CNSX/depth-price/';

"""
Base URL for last closing data
"""
URL_HISTORIES = 'http://thecse.com/mssql/get/CNSX/histories/';

"""
Base URL for stock listings
"""
URL_LISTINGS = 'http://thecse.com/sites/default/files/documents/activity_summaries/CSE_Listed/CSE%20Stock%20List.xls'

"""
Base URL for last 25 trades
"""
URL_LAST_TRADES = 'http://thecse.com/mssql/get/CNSX/lasttrade/';

"""
Base URL for quotes
"""
URL_QUOTE = 'http://thecse.com/cmsAssets/CustomUserControls/UserModules/CNSX_Securities/WCF/WCF_CNSX.svc/GetStockQuote/?Therefore-func=True&SymbolName='

# HTTP header data for all requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

def getJson(url, ticker):
    """
    :param url: str
    :param ticker: str
    """
    url = f'{url}{ticker}'
    r = requests.get(url, headers=headers)
    return json.loads(r.text)

def getChart(ticker):
    """
    :param ticker: str
    Return:
    [
        {
            security_moniker: "2015-12-31:BE",
            date: "2016-10-17T00:00:00.000Z",
            time: "15:56:12.471000",
            volume: 4000,
            price: 1.13,
            buy_dealer: "TD Securities Inc.",
            sell_dealer: "Anonymous",
            tick: 0,
            trade_or_quote_id: "135695110",
            value: "4520",
            change: -0.03,
            tradetimestamp: 1476734172
        },
        {
            security_moniker: "2015-12-31:BE",
            date: "2016-10-19T00:00:00.000Z",
            time: "15:59:04.417000",
            volume: 1000,
            price: 1.03,
            buy_dealer: "W.D. Latimer Co. Limited",
            sell_dealer: "RBC Capital Markets",
            tick: -0.01,
            trade_or_quote_id: "140016061",
            value: "1030",
            change: -0.11,
            tradetimestamp: 1476907144
        }
    ]
    """
    return getJson(URL_CHART, ticker)

def getDepth(ticker):
    """
    :param ticker: str
    Returns:
    [
        {
            Bid Dealer: "Questrade Inc.",
            Bid Size: "200",
            Bid Price: "1.810",
            Ask Price: "1.830",
            Ask Size: "22,700",
            Ask Dealer: "TD Securities Inc."
        },
        {
            Bid Dealer: "W.D. Latimer Co. Limited",
            Bid Size: "1,000",
            Bid Price: "1.810",
            Ask Price: "1.830",
            Ask Size: "5,000",
            Ask Dealer: "TD Securities Inc."
        }
    ]
    """
    return getJson(URL_DEPTH, ticker)

def getDepthPrice(ticker):
    """
    :param ticker: str
    Returns:
    [
        {
            Bid Count: "4",
            Bid Size: "4,900",
            Bid Price: "1.810",
            Ask Price: "1.830",
            Ask Size: "33,100",
            Ask Count: "4"
        },
        {
            Bid Count: "5",
            Bid Size: "21,500",
            Bid Price: "1.800",
            Ask Price: "1.840",
            Ask Size: "32,000",
            Ask Count: "2"
        }
    ]
    """
    return getJson(URL_DEPTH_PRICE, ticker)

def getHistories(ticker):
    """
    :param ticker: str
    Return"
    [
        {
            date: "2017-10-13T00:00:00.000Z",
            symbol: "BE",
            currency: "CAD",
            shares_in_the_index: "5.388603",
            opening_price: "1.89",
            previous_closing_price: 1.85,
            last_price: "1.81",
            last_tick: "-0.02",
            days_low_price: "1.81",
            days_high_price: "1.89",
            historical_52_week_low_price: "0.72",
            historical_52_week_high_price: "2.85",
            trade_count: "105",
            security_name: "Beleave Inc.",
            moniker: "2015-12-31:BE",
            trading_volume: 132604,
            trading_value: 243046.71,
            trading_value_cad: 243046.71,
            id: 256221
        }
    ]
    """
    return getJson(URL_HISTORIES, ticker)

def getListings():
    """
    :param ticker: str
    Returns:
    """
    return requests.get(URL_LISTINGS, headers=headers).text

def getLastTrades(ticker):
    """
    :param ticker: str
    Returns:
    [
        {
            security_moniker: "2015-12-31:BE",
            date: "2017-10-13T00:00:00.000Z",
            time: "15:53:47.682000",
            volume: 200,
            price: 1.81,
            buy_dealer: "TD Securities Inc.",
            sell_dealer: "TD Securities Inc.",
            tick: -0.02,
            trade_or_quote_id: "764732505",
            value: "362",
            change: -0.04,
            timestamp: 1507924427000
        },
        {
            security_moniker: "2015-12-31:BE",
            date: "2017-10-13T00:00:00.000Z",
            time: "15:50:59.207000",
            volume: 200,
            price: 1.83,
            buy_dealer: "Questrade Inc.",
            sell_dealer: "TD Securities Inc.",
            tick: 0.01,
            trade_or_quote_id: "764713765",
            value: "366",
            change: -0.02,
            timestamp: 1507924259000
        }
    ]
    """
    return getJson(URL_LAST_TRADES, ticker)

def getQuote(ticker):
    """
    :param ticker: str
    Returns:
    {
        date: "2017-10-13T00:00:00.000Z",
        symbol: "BE",
        currency: "CAD",
        shares_in_the_index: "5.388603",
        opening_price: "1.89",
        previous_closing_price: 1.85,
        last_price: "1.81",
        last_tick: "-0.02",
        days_low_price: "1.81",
        days_high_price: "1.89",
        historical_52_week_low_price: "0.72",
        historical_52_week_high_price: "2.85",
        trade_count: "105",
        security_name: "Beleave Inc.",
        moniker: "2015-12-31:BE",
        trading_volume: 132604,
        trading_value: 243046.71,
        trading_value_cad: 243046.71,
        id: 256221,
        Volume: 132604,
        High_52Week: "2.85",
        Low_52Week: "0.72",
        LastPrice: 1.81,
        NetChange: -0.04,
        BidPrice: 1.81,
        BidSize: 4900,
        AskSize: 33100,
        AskPrice: 1.83,
        TickStatus: -1,
        TimeStamp: "/Date(1507925327-0500)/"
    }
    """
    return getJson(URL_QUOTE, ticker)
