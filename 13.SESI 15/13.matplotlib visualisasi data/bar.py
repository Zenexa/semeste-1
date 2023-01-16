import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('E:\\Data_siswa_unp.csv')

# data.head()
# data.shape

x = data['Jurusan']
y = data['Jumlah']

plt.bar(x,y)
plt.show()


