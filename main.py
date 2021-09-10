from data import dataframes
from data import precios_mensuales
import math as m
import data as dt

data_ini = dataframes['NAFTRAC_20180131']['Peso (%)']
data_ini = data_ini.drop([10, 35]).reset_index(drop=True)
pond_money = dt.capital * data_ini
price_per_shares = precios_mensuales.iloc[0, :]

num_shares = [pond_money[i] / price_per_shares[i] for i in range(0, len(pond_money))]
num_shares = [m.trunc(num_shares[i]) for i in range(0, len(pond_money))]

cms = sum(num_shares * price_per_shares * dt.comision)

money_cash = dt.capital - sum(num_shares * price_per_shares) - dt.comision

port_value_ini = sum(num_shares * price_per_shares) + money_cash

port_value = [sum(precios_mensuales.iloc[i, :] * num_shares) for i in range(1, len(precios_mensuales))]
port_value.insert(0, port_value_ini)