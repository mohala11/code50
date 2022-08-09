import json
import requests
import sys


try:
    x = float(sys.argv)
except ValueError:
    sys.exit("dolbaeb")


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
