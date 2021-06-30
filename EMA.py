import pandas as pd
import numpy as np

data = np.linspace(0,40,num = 40)
df = pd.DataFrame({'A':data})

#def MACD(span_short=12,span_long=26,span_dif = 9):
span_short = 12
span_long=26
span_dif = 9
EMA_short = df.ewm(span=span_short,adjust = False).mean()
EMA_long = df.ewm(span=span_long,adjust = False).mean()
dif = EMA_short - EMA_long
dea = dif.ewm(span = span_dif, adjust = False).mean()
macd = (dif - dea) * 2
macd.plot.line