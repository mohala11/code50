import json
import requests
import sys


try:
    y = float(sys.argv[1])
except ValueError:
    sys.exit("")


r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = r.json()
z = float(o["bpi"]["USD"]["rate_float"])
print(z*y)
