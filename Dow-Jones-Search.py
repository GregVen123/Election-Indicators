import numpy as np
import pandas as pd
from openpyxl import *
import plotly.express as px
df = pd.read_csv("DJIA88-24.csv")
close_prices = np.array(df[" Close"])
DJIA_dates = df.Date
dict1 = {
    "Date": DJIA_dates,
    "Price": close_prices
}
df2 = pd.DataFrame(data=dict1)
year_index = []
for i in range(10):
    year_index.append(252*4*i)
election_year =[2024,2020,2016,2012,2008,2004,2000,1996,1992,1988]
dates_in_days = [[],[],[],[],[],[],[],[],[]]
for i in range(len(year_index)-1):
    dates_in_days[i].append(year_index[i])
    dates_in_days[i].append(year_index[i+1])

test2 = df2.iloc[dates_in_days[0][0]:dates_in_days[0][1]]
print(test2)

fig = px.line(x=test2.index[::-1], y=test2["Price"])
fig.show()
#test3 = df2[df2["Price"]>30000]
#print(test3)
