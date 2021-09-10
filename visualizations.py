import pandas as pd
from main import port_value_ini, port_value
from data import precios_mensuales, capital

df = pd.DataFrame({"Timestamp": precios_mensuales.index, "Capital": port_value})

rend = [(port_value[i+1] / port_value[i]) - 1 for i in range(0, len(port_value)-1)]
rend.insert(0, 0)

rend_acum = [(port_value[i] / port_value_ini)-1 for i in range(0, len(port_value))]
rend_fin = [df["Capital"][i]- capital for i in range(0, len(port_value))]

df["Rend"] = rend
df["Rend_acum"] = rend_acum
df["Ganancia/Perdida $"] = rend_fin

