import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
start = datetime.datetime(2007,1,1)
end = datetime.datetime(2018,1,1)
symbol = 'WIKI/AAPL'
f = pdr.DataReader(symbol, 'quandl', start, end)
f['Diff'] = f.Open-f.Close
f['Close'].plot(grid = True)
plt.show()