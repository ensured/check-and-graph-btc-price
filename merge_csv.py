import datetime
import getpass
import glob
import os
from pathlib import Path

import pandas as pd

# get computer name
user = getpass.getuser()

# create directory for all merged data to go
os.makedirs("C:\\Users\\" + user + "\\Desktop\\btc\\merged_data", exist_ok=True)

# datetime stuff
now = datetime.datetime.now()
f_now = str(now.strftime("%I_%M%p"))
dt_now = datetime.datetime.today()
date = str(dt_now.year) + "-" + str(dt_now.month) + "-" + str(dt_now.day)

# read all .scv files from this path
dir = Path("C:\\Users\\" + user + "\\Desktop\\btc\\all_data")

# read all .scv files
df = (pd.read_csv(f, names=["DATE", "TIME", "PRICE"]) for f in dir.glob("*.csv"))

# concatenation
all_data = pd.concat(df, sort=True, ignore_index=True)

# merge all concatenated data to single csv
all_data.to_csv(f"merged_data\\btc_all_data__{date}__{f_now}.csv")
print("Done merging everything in 'btc\\all_data' folder.")
