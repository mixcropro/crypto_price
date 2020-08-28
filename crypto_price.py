import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

coin = input("\nWhat coin would you like to check? ")

url = "https://www.coingecko.com/en/coins/" + coin
request = requests.get(url)
s = bs(request.text, "html.parser")
btc = s.find_all("span", class_="no-wrap")

current_price = btc[0].text.strip()
ath_price = btc[14].text.strip()
ath_price_cash = str(ath_price[1:])
ath_price_cash_new = float(ath_price_cash.replace(",",""))

print(coin + " price on " + dt_string + " at " + current_time + " is: " + current_price)
print(coin + " ath was: " + ath_price)
current_x = float(input("How many coins do you have right now? "))
possible_cashMoney = ath_price_cash_new * current_x
print("You could've had " + str(possible_cashMoney)  + "$ if you bought on ATH!")
