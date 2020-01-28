from time import sleep
import creds
import SMS
from yahoo_fin import stock_info as si

stockTargets = {
    "aapl": 307,
    "amzn": 1815,
    "msft": 158,
    "fb": 210,
    "goog": 1420,
    "ibm": 135,
    "tsla": 550,
    "intc": 60,
    "amd": 45

}


def check_price():
    appl = round(si.get_live_price("aapl"), 3)
    amzn = round(si.get_live_price("amzn"), 3)
    msft = round(si.get_live_price("msft"), 3)
    fb = round(si.get_live_price("fb"), 3)
    goog = round(si.get_live_price("goog"), 3)
    ibm = round(si.get_live_price("ibm"), 3)
    tsla = round(si.get_live_price("tsla"), 3)
    intel = round(si.get_live_price("intc"), 3)
    amd = round(si.get_live_price("amd"), 3)

    # get most active stocks on the day
    active = si.get_day_most_active()

    # get biggest gainers
    gainers = si.get_day_gainers()

    # get worst performers
    losers = si.get_day_losers()

    stocksUpdate = """Hello, here are the current stock prices:
        Apple: {appl}
        Amazon: {amzn}
        Microsoft: {msft}
        Facebook: {fb}
        Google: {goog}
        IBM: {ibm}
        Tesla: {tsla}
        Intel: {intel}
        AMD:{amd}
    """.format(appl=appl, amzn=amzn, msft=msft, fb=fb, goog=goog, ibm=ibm, tsla=tsla,
               intel=intel, amd=amd)

    fullStocksUpdate = """ 
    Hello, here are the current stock prices:
        Apple: {appl}
        Amazon: {amzn}
        Microsoft: {msft}
        Facebook: {fb}
        Google: {goog}
        IBM: {ibm}
        Tesla: {tsla}
        Intel: {intel}
        AMD:{amd}
    
    Most active: \n {active}
    Biggest Gainers: \n {gainers}
    Biggest Losers: \n {losers}
    
    """.format(appl=appl, amzn=amzn, msft=msft, fb=fb, goog=goog, ibm=ibm, tsla=tsla,
               intel=intel, amd=amd, active=active, gainers=gainers, losers=losers)
    msg = f"Subject: {'Stock Prices'}\n\n{stocksUpdate}"
    SMS.send(msg)
    print(stocksUpdate)


# n = int(input("Enter the number of stocks you want watched: "))

# for i in range(0, n):
#     stock = input("Stock " + str(i) + " ticker: ")
#     price = int(input("Target price: "))

#     stockTargets[stock] = price

# for x in stockTargets:
#     print(x + " "+str(stockTargets[x]))

while True:
    check_price()
    sleep(30*60)
