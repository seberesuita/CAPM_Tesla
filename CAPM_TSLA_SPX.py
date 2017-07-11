import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

tesla_main = pd.read_csv('Files/TSLA_DAILY_1517.CSV',index_col="Date",usecols=['Date','Adj Close'],
                         parse_dates=True)
spx_main = pd.read_csv('Files/SPX_DAILY_1517.CSV',index_col="Date",usecols=['Date','Adj Close'],
                         parse_dates=True)

'''Tesla Daily Return calculation > renaming column > convert to percentage'''
tsla_daily_return = tesla_main.pct_change(1)
tsla_daily_return = tsla_daily_return.rename(columns={'Adj Close':'TESLA Daily Return'})
tsla_daily_return['TESLA Daily Return'] = tsla_daily_return['TESLA Daily Return'] * 100

'''SPX Daily Return calculation > renaming column > convert to percentage'''
spx_daily_return = spx_main.pct_change(1)
spx_daily_return = spx_daily_return.rename(columns= {'Adj Close':'SPX Daily Return'})
spx_daily_return['SPX Daily Return'] = spx_daily_return['SPX Daily Return'] * 100

df_spx = spx_main.join(spx_daily_return, how='inner')
df_tsla = tesla_main.join(tsla_daily_return, how ='inner')
df_tsla = df_tsla.rename(columns={'Adj Close':'TSLA Adj Close'})
df_spx = df_spx.rename(columns = {'Adj Close':'SPX Adj Close'})

df_main = df_spx.join(df_tsla, how = 'inner')


x = df_main['SPX Daily Return']
y = df_main['TESLA Daily Return']
colors = (0,0,0,)
area = np.pi*3

plt.scatter(x,y,s =area, c = colors, alpha=.5)
plt.ylabel('TSLA Daily Return')
plt.xlabel('SPX Daily Return')
plt.title('CAPM Model for Tesla Motors')
plt.show()

sea_date = df_main[['TESLA Daily Return','SPX Daily Return']]

sea_date =sea_date.rename(columns={'TESLA Daily Return':'TSLA'})
sea_date =sea_date.rename(columns={'SPX Daily Return':'SPX'})

new_frame =pd.DataFrame[sea_date.filter(['TSLA','SPX'],axis = 1)]
print new_frame

xdata = sb.load_dataset(new_frame)
ax = sb.regplot(x="SPX", y="Tsl", data=xdata)




'''
def test_run():
    df_main[['SPX Daily Return','TESLA Daily Return']].plot()
    plt.xlabel('Dates')
    plt.ylabel('Daily Return')

    plt.show()

if __name__ == '__main__':
    test_run()
'''
