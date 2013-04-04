import urllib.request
import time

price = 99
while price > 4:
    
    time.sleep(900)
    
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find(">$")

    pricestart = where + 2
    priceend = pricestart + 4

    price = float(text[pricestart:priceend])
    
print("Buy")    
