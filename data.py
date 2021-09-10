import pandas as pd
import numpy as np
from functions import get_adj_closes
import yfinance as yf

# Se define el Capital, comision y tasa libre de riesgo
capital = 1000000
comision = 0.00125 # comision a cobrar cada que se realice una compra de títulos
rf = 0.0429

# Listado de nombres de archivo
archivos = ['NAFTRAC_20180131', 'NAFTRAC_20180228', 'NAFTRAC_20180328', 'NAFTRAC_20180430', 'NAFTRAC_20180531',
            'NAFTRAC_20180629', 'NAFTRAC_20180731', 'NAFTRAC_20180831', 'NAFTRAC_20180928', 'NAFTRAC_20181031',
            'NAFTRAC_20181130', 'NAFTRAC_20181231', 'NAFTRAC_20190131', 'NAFTRAC_20190228', 'NAFTRAC_20190329',
            'NAFTRAC_20190430', 'NAFTRAC_20190531', 'NAFTRAC_20190628', 'NAFTRAC_20190731', 'NAFTRAC_20190830',
            'NAFTRAC_20190930', 'NAFTRAC_20191031', 'NAFTRAC_20191129', 'NAFTRAC_20191231', 'NAFTRAC_20200131',
            'NAFTRAC_20200228', 'NAFTRAC_20200331', 'NAFTRAC_20200430', 'NAFTRAC_20200529', 'NAFTRAC_20200630',
            'NAFTRAC_20200731', 'NAFTRAC_20200831', 'NAFTRAC_20200930', 'NAFTRAC_20201030', 'NAFTRAC_20201130',
            'NAFTRAC_20201231', 'NAFTRAC_20210129', 'NAFTRAC_20210226', 'NAFTRAC_20210331']

dataframes = {}
for i in archivos:
    data = pd.read_csv('files/' + i + '.csv',
                       skiprows=2,
                       usecols=['Ticker', 'Peso (%)']).dropna()
    data_ty = {'Ticker': str, 'Peso (%)': float}
    data = data.astype(data_ty)
    data['Ticker'] = [i.replace('*', '') for i in data['Ticker']]
    data['Ticker'] = data['Ticker'] + '.MX'
    data['Ticker'] = [i.replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX') for i in data['Ticker']]
    data['Peso (%)'] = data['Peso (%)'] / 100
    dataframes[i] = data

t = []
for i in archivos:
    t.append(dataframes[i]['Ticker'])

tickers = np.unique(t[0]).tolist()
tickers = [i.replace('*', '') for i in tickers]
tickers = [i.replace('LIVERPOLC.1.MX', 'LIVERPOLC-1.MX') for i in tickers]
tickers = [i.replace('GFREGIOO.MX', 'RA.MX')for i in tickers]
tickers = [i.replace('MEXCHEM.MX', 'ORBIA.MX') for i in tickers]
[tickers.remove(i) for i in ['KOFL.MX', 'MXN.MX']]


precios_mensuales = pd.DataFrame(get_adj_closes(tickers=tickers, start_date="2018-01-31", end_date="2021-01-31"))
precios_mensuales = precios_mensuales.groupby(pd.Grouper(freq="M")).last()



