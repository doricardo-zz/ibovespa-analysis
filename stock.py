#https://medium.com/@cesar.vieira/o-coeficiente-beta-como-comparar-a%C3%A7%C3%B5es-com-o-mercado-local-3cd4d1230b68

#O coeficiente beta: como comparar ações com o mercado local

import pandas as pd
from pandas_datareader import data as wb

from matplotlib import pyplot as plt

import numpy as np

Inicio  = '2019-09-17'
Final   = '2019-10-19'
TickerA = 'EVEN3.SA' #ativo A
TickerB = 'VVAR3.SA' #ativo B
TickerC = '^BVSP'    #mercado

tickers = [TickerA, TickerB, TickerC]


data = pd.DataFrame()

for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start = Inicio, end = Final )['Adj Close']


datanorm=data/data.iloc[0]*100
datanorm.plot(figsize=(12,5))
plt.xlabel('DATE')
plt.ylabel('NORMALIZED INDEXES')
plt.show()


log_returns = np.log(data/data.shift(1))
log_returns.plot(figsize=(12,5))
plt.xlabel('DATE')
plt.ylabel('LOG RETURNS')
plt.show()


cov = log_returns.cov()*250             #covariância dos dados
var_m = log_returns[TickerC].var()*250  #variância do mercado

print(cov)


Am_cov = cov.iloc[0,2]   #Am_cov : covariância('ITSA4.SA' x ^BVSP)
Bm_cov = cov.iloc[1,2]   #Bm_cov :covariância('CIEL3.SA' x ^BVSP)
A_beta = Am_cov/var_m
B_beta = Bm_cov/var_m

print(A_beta)
print(B_beta)
