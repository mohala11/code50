import requests
import sys


try:
    y = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = r.json()
z = float(o["bpi"]["USD"]["rate_float"])
summ = z*y
print(f"${summ:,}")

