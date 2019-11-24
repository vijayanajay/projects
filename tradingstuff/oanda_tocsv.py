import oandapy
import csv

oanda = oandapy.API(environment="practice", access_token="1816a9d5b9499beab43c676a1f329525-de17d9cda518706af6b85740c8757372")

response = oanda.get_history(instrument="EUR_USD", granularity ="M1", count = 5000)

prices = response.get("candles")

print (response)

keys=prices[0].keys()

with open('EUR_USD.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    for items in prices:
        writer.writerow(items)