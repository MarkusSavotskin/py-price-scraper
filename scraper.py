import os
import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.hinnavaatlus.ee/products/Arvutikomponendid/Protsessorid/2cae0b3c627772d7cfcad95f4f7e38d7/?sort=-views"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")


def get_prices():
    title = soup.find_all("div", class_="price price-large")
    title.append(soup.find_all("div", class_="price price-large with-change"))
    prices = []
    for price in title:
        prices.append(str(price).split(">")[1].split("<")[0])
    return prices


def currect_prices():
    print("Current Ryzen 5 5600 prices:")
    for price in old_prices:
        print(price)


minutes = 5

old_prices = get_prices()
new_prices = []

while True:
    if minutes == 0:
        new_prices = get_prices()
        for i in range(len(old_prices)):
            if old_prices[i] != new_prices[i]:
                new_prices[i] = f"{old_prices[i]} -> {new_prices[i]}"
            if int(new_prices[i].split(",")[0]) <= 200:
                print("PRICE UNDER 200.\n" * 20)
                break
        old_prices = new_prices
        minutes = 5
    os.system("cls")
    currect_prices()
    print(f"Updating prices in {minutes} minutes...")
    time.sleep(60)
    minutes -= 1
