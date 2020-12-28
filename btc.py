import requests
from time import sleep
import datetime
import os
import getpass

user = getpass.getuser()

# get current working directy
cwd = os.getcwd()
os.makedirs(f"{cwd}\\all_data", exist_ok=True)
btc_data_path = f"{cwd}\\all_data"


def GET_RATES():
    url = requests.get("http://preev.com/pulse/units:btc+usd/sources:bitstamp+kraken")
    data = url.json()
    result = {}
    for rates in data["btc"]["usd"].values():
        result = float(rates["last"])
    return result


def log_and_print_GET_RATES():
    v = 10
    while v > 0:
        now = datetime.datetime.now()
        dt = datetime.datetime.today()
        date = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + ","
        date2 = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        formatted_date = date + now.strftime("%I:%M:%S%p")
        print(
            str(formatted_date) + "," + str(GET_RATES()),
            file=open(f"{btc_data_path}\\btc_prices_{date2}.csv", "a+"),
        )  # Logs time and current btc price to a file.
        print(str(formatted_date) + "," + str(GET_RATES()))
        sleep(0.5)
    else:
        print("")


log_and_print_GET_RATES()
