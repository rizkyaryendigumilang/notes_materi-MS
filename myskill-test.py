import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 



## Probality : kemukingan yang akan terjadi 

## 2. Discrete Distribusi meuruk tersebasarn tertentu >> histogram
from scipy.stats import bernoulli
koin = bernoulli.rvs(size = 100, p = 0.5)
#plot
sns.hisplot(koin)
plt.show()

koin


## 3. binomial > bernouli yang banyak pengulanganya banyak 2 koin dari distribusi bernouli 
from scipy.stats import binom
koin = binom.rvs(size = 1000, n=10, p = 0.5)
#plot
sns. hisplot (koin)
plt.show()

## 4. Distribusi Poisson Prediksi barang cacat (berapa banyak kejadian dari sebuah interval)
from scipy.stats import poisson
cacat = poisson.rvs(size = 100, mu = 2) #mu= rata2
#plot
sns.hisplot (cacat)
plt.show()

## 5. distribusi yang memiliki peluang yang sama untuk nilai yang berbeda [0-9] setiap angka memiliki peluang
##      untuk terpilih

from scipy.stats import uniform
uniform_data = uniform.rvs(size = 1000, loc = 0, scale = 9)
#plot 
sns.hisplot(uniform_data)
plt.show() 

## 6. normal distribustion seperti lonceng dan sering digunakan untuk banyak kejadian atau sebuah interval
from spicy.stats import norm
kejadian = norm.rvs(size = 1000, loc = 70, scale = 10)
##plot
sns.hisplot (kejadian)
plt.show()






                                    ## Rata-Rata
nilai = [74, 49, 68, 86, 80, 71, 77, 81, 72, 77]
x-bar = np.mean(nilai)
