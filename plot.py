import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.style
import datetime

# datetime stuff
now = datetime.datetime.now()
# f_now = str(now.strftime("%I_%M%p")) # time of day but not using
dt_now = datetime.datetime.today()
date = str(dt_now.year) + "-" + str(dt_now.month) + "-" + str(dt_now.day)


def count_lines():
    num_lines = sum(1 for line in open(f"merged_data\\btc_all_data__{date}.csv"))
    return f"line count: {num_lines}"


print(count_lines())

plt.style.use("dark_background")

df = pd.read_csv(f"merged_data\\btc_all_data__{date}.csv")
df.plot(x="TIME", y=["PRICE"], title="BTC PRICE LINE GRAPH")
plt.show()