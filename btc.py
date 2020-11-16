import requests
from time import sleep
import datetime
import getpass

print('''

  _       _                             _                          _                     _                     __  _   _   ____    ____   __  
 | |__   | |_    ___     _ __    _ __  (_)   ___    ___      ___  | |__     ___    ___  | | __   ___   _ __   / / | | | | / ___|  |  _ \  \ \ 
 | '_ \  | __|  / __|   | '_ \  | '__| | |  / __|  / _ \    / __| | '_ \   / _ \  / __| | |/ /  / _ \ | '__| | |  | | | | \___ \  | | | |  | |
 | |_) | | |_  | (__    | |_) | | |    | | | (__  |  __/   | (__  | | | | |  __/ | (__  |   <  |  __/ | |    | |  | |_| |  ___) | | |_| |  | |
 |_.__/   \__|  \___|   | .__/  |_|    |_|  \___|  \___|    \___| |_| |_|  \___|  \___| |_|\_\  \___| |_|    | |   \___/  |____/  |____/   | |
                        |_|                                                                                   \_\                         /_/ 

''')
current_user = getpass.getuser()
print(f"    Welcome {current_user}!!\n".upper())
print('''
    This script I made checks the bitcoin price roughly once every second
    and conveniently logs it to a .txt file and prints it to the screen.\n
    Entering 10000 will check the price 1 million times :P
    Entering .02 will check the price 2 times.\n\n
''')

def GET_RATES():
    url = requests.get('http://preev.com/pulse/units:btc+usd/sources:bitstamp+kraken')
    data = url.json()
    result = {}
    for exchange, rates in data['btc']['usd'].items():
        result[exchange] = float(rates['last'])
    return result


def log_and_print_GET_RATES():
    user_run_amount = float(input("Enter .01 or >: "))
    user_run_amount = user_run_amount * 100
    while user_run_amount > 0:
        chosen_file = "btc_price.txt" # specify where you want to save btc price.
        my_file = open(chosen_file, "a")
        now = datetime.datetime.now()
        now = now.replace(microsecond=0) # datetime.now without microsecond.
        print(now, GET_RATES(), file=my_file) # Logs time and current btc price to a file.
        print(now, GET_RATES())
        sleep(.5)
        user_run_amount -= 1
    else:
        print(f'While loop ended and reached "{user_run_amount}"')
        my_file.close()
        print("Closed file. ")

log_and_print_GET_RATES()
