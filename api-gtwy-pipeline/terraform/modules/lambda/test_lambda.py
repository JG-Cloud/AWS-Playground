import requests
import freecurrencyapi
import os
from pprint import pprint

# Currency API source: https://exchangerate.host

url = 'https://api.exchangerate.host/latest/?base=GBP'
response = requests.get(url)
data = response.json()

allrates = data['rates']

for currency, rate in allrates.items():
    if 'AED' in currency:
        AEDrate = rate
    
    if 'USD' in currency:
        USDrate = rate
          
print(f"Base currency is GBP:")
print(f"AED : {AEDrate}")
print(f"USD : {USDrate}")