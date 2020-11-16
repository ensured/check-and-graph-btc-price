import requests
from time import sleep
import datetime
import getpass


current_user = getpass.getuser()
print(f"Welcome to btc checker {current_user}!\n".upper())
print("This script I made checks the bitcoin price roughly once every second\nand conveniently logs it to a .txt file and prints it to the screen.\n")

def GET_RATES():
    url_resp = requests.get('http://preev.com/pulse/units:btc+usd/sources:bitstamp+kraken') # (your url)
    data = url_resp.json()
    result = {}
    for exchange, rates in data['btc']['usd'].items():
        result[exchange] = float(rates['last'])
    return result

print("Entering 10000 will check the price 1 million times :P\nEntering .02 will check the price 2 times.\n")
def log_and_print_GET_RATES():
    user_run_amount = float(input("Enter .01 or >: "))
    user_run_amount = user_run_amount * 100
    while user_run_amount > 0:
        now = datetime.datetime.now()
        now = now.replace(microsecond=0) # Print datetime.now without microsecond.
        print(now, GET_RATES(), file=open("btc_price.txt", "a"))
        print(now, GET_RATES())
        sleep(.5)
        user_run_amount -= 1
    else:
        print(f'Loop ended: "{user_run_amount}"')

log_and_print_GET_RATES()