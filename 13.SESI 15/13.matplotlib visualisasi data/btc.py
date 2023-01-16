import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('E:\\BTC-USD.csv')
dataNew = data[['Date','High','Low','Close','Volume']]
print(dataNew)

plt.plot(dataNew['High'],dataNew['Low'])
plt.show()
#x = data['Date']
#y = data['High']

#plt.bar(x,y)
#plt.show()
