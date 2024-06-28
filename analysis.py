import pandas as pd

nifty = pd.read_csv('NIFTY FMCG.csv')
print(nifty)
nifty['Date'] = pd.to_datetime(nifty['Date'])
nifty['year'] = nifty['Date'].dt.year
print(nifty)
print('--------------')
nifty = (nifty.groupby('year').first())
nifty = nifty.dropna()

nifty['Return'] = ((50000/nifty['Open'])*nifty['Open'].iloc[-1])
nifty['Investment'] = 50000
print('----------------------')
print('-----------------------')
print(nifty)

s = (nifty['Return'].sum())
p = (nifty['Investment'].sum())
print('------------------')
print("Return",s)
print("Investment", p)
ROI = s-p
print("Profit",ROI)
 
percent = (ROI/p)*100
print(percent) 





