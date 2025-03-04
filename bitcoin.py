import requests
import sys


if len(sys.argv) == 2:
    try:  
        btc_wanted = float(sys.argv[1])
    except: 
        sys.exit("Argument not numeric")
else:
    sys.exit("2 arguments not provided")

try:
    btc_rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    sys.exit("Something went wrong with the request")

try:
    btc_rate_eur = btc_rate["bpi"]["EUR"]["rate_float"]
except:
    sys.exit("Something wrong with getting desired object from Response")


def get_cost(btc_wanted: float, btc_rate: float) -> float:
    return f"${round(float(btc_wanted) * float(btc_rate), 5):,.4f}"


print(get_cost(btc_wanted=btc_wanted, btc_rate=btc_rate_eur))