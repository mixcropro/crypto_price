import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

def btc():
    url = "https://www.coingecko.com/en/coins/bitcoin" #->change url of the wanted coin
    request = requests.get(url)
    s = bs (request.text, "html.parser")
    btc = s.find_all("span", class_="no-wrap")

    current_price = btc[0].text.strip()
    ath_price = btc[14].text.strip()
    ath_price_cash = str(ath_price[1:-3]) #-> careful when copying this for other currencies!! do this if the price ends with  eg .22
    ath_price_cash_new = float(ath_price_cash.replace(",","")) #-> do this only if there are , in number else just dont put this line in function


    print("BTC price on: " + dt_string + " at " + current_time + " is: " + current_price) #-> change BTC to wanted coin alias to avoid mistakes (price will be still good)
    print("BTC ath was: " + ath_price)
    current_x = float(input("How many coins do you have right now? "))
    possible_cashMoney = ath_price_cash_new * (current_x)
    print("You would have " + str(possible_cashMoney) + " if you bought on ATH!")

def eth():
    url = "https://www.coingecko.com/en/coins/ethereum"
    request = requests.get(url)
    s = bs(request.text, "html.parser")
    btc = s.find_all("span", class_="no-wrap")

    current_price = btc[0].text.strip()
    ath_price = btc[14].text.strip()
    ath_price_cash = str(ath_price[1:-3])
    ath_price_cash_new = float(ath_price_cash.replace(",", ""))

    print("ETH price on: " + dt_string + " at " + current_time + " is: " + current_price)
    print("ETH ath was: " + ath_price)
    current_x = float(input("How many coins do you have right now? "))
    possible_cashMoney = ath_price_cash_new * (current_x)
    print("You would have " + str(possible_cashMoney) + " if you bought on ATH!")

def xrp():
    url = "https://www.coingecko.com/en/coins/xrp"
    request = requests.get(url)
    s = bs(request.text, "html.parser")
    btc = s.find_all("span", class_="no-wrap")

    current_price = btc[0].text.strip()
    ath_price = btc[14].text.strip()
    ath_price_cash = ath_price[1:] #-> do this if there are no , in number else check btc for more info
    ath_price_cash_neww = float(ath_price_cash)

    print("XRP price on: " + dt_string + " at " + current_time + " is: " + current_price)
    print("XRP ath was: " + ath_price)
    current_x = float(input("How many coins do you have right now? "))
    possible_cashMoney = ath_price_cash_neww * (current_x)
    print("You would have " + str(possible_cashMoney) + " if you bought on ATH!")



#defing a new function preferably named after wanted coin alias and just copy paste everything, but dont forget to change url for the correct coin!!!
#and then add a new elif condition!!

while True:
    coin = input("\nWhat coin would you like to check? ")
    if coin == "btc":
        btc()
    elif coin =="eth":
        eth()
    elif coin == "xrp":
        xrp()
    else:
        break
