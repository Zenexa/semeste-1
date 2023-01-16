import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

#for dir
df = pd.read_csv('E:\\BTC-USD.csv')
df

#for x and y
x = df['Date'] 
y = df['High']

#type diagram
plt.bar(x,y,width = 0.5)

#set label
plt.xlabel('HIGH AND LOW')
plt.title('BTC PRICE FROM 2014 - 2022 ')

#for showing graphic
plt.show()
