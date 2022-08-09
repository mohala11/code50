import json
import requests
import sys


try:
    y = float(sys.argv[1])
    print(y)
except ValueError:
    sys.exit("error")


r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = r.json()
for result in o[""]:
    print(result[])
