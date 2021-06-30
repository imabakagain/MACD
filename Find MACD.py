import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

pro = ts.pro_api()
def stock_monthly(code,st_date,En_date):
    def Signal(code):
        stack = macd[-3:].tolist()
#        print(stack)
        if all([m< -0.5*mean for m in stack]):
            if stack.index(min(stack)) == 1:
                print('Buy signal in', code)
                return True
            else :
                return False
    #Get stock info
    df = pro.monthly(ts_code = code, adj = 'qfq', start_date = st_date, end_date = En_date)
    df_close = df[['trade_date','close']]
    df_close = df_close.loc[::-1].reset_index(drop = True)
    df_close.columns=['ds','y']
    #    plt.plot(df_close.ds, df_close.y)
    #    plt.show()

    #MACD and processing
    exp1 = df_close.y.ewm(span=12, adjust=False).mean()
    exp2 = df_close.y.ewm(span=26, adjust=False).mean()

    dif = exp1-exp2
    dea = dif.ewm(span=9, adjust=False).mean()
    macd = (dif-dea) * 2
#    print(macd)
    macd_abs = abs(macd)
    mean = np.mean(macd_abs)
#    print('mean',mean)
    for macd_t in macd:
        if (macd_t == 0):
            macd_t = 0.01
    return Signal(code)
