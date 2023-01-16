import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('E:\\Data_siswa_unp.csv')

data.head()
data.shape

jurusan = data['Jurusan']
jumlah = data['Jumlah']

plt.pie(jumlah,labels = jurusan)
plt.show()


