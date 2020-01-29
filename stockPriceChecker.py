import time
import datetime
import creds
import SMS
from yahoo_fin import stock_info as si

# Defining business hours start  & end time
start = datetime.time(9, 30, 0)
end = datetime.time(16, 30, 0)

# Creating dictionary that will hold tickers & prices
stockTickers = {
    "aapl": "aapl",
    "amzn": "amzn",
    "msft": "msft",
    "fb": "fb",
    "goog": "goog",
    "ibm": "ibm",
    "tsla": "tsla",
    "intc": "intc",
    "amd": "amd"

}

# Populating dictionary with prices
for i in stockTickers:
    stockTickers[i] = round(si.get_live_price(i), 3)


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def check_price():
    # Updating prices
    for i in stockTickers:
        stockTickers[i] = round(si.get_live_price(i), 3)

    # Creating message to send
    stocksUpdate = """Apple: {appl}, Amazon: {amzn}  Microsoft: {msft} Facebook: {fb} Google: {goog} IBM: {ibm} Tesla: {tsla} Intel: {intel}, AMD:{amd}
    """.format(appl=stockTickers["aapl"], amzn=stockTickers["amzn"], msft=stockTickers["msft"], fb=stockTickers["fb"],
               goog=stockTickers["goog"], ibm=stockTickers["ibm"], tsla=stockTickers["tsla"], intel=stockTickers["intc"], amd=stockTickers["amd"])

    msg = f"Subject: {'Stock Prices'}\n\n{stocksUpdate}"

    # Sending message
    SMS.send(msg)
    print(stocksUpdate)


# Main
while True:
    # check if current time is within business hours
    now = datetime.datetime.now().time()
    if time_in_range(start, end, now):
        check_price()
        time.sleep(60*60)

    # If not, sleep for 30 mins
    else:
        print('TEST')
        time.sleep(30*60)
