
#from elementwise import *

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
import matplotlib.ticker as ticker


data_ac=pd.read_csv('./Test.csv', encoding='latin1', parse_dates=[['Date','Time']], dayfirst=True)
# print(data_ac)
##C1
horaC1= data_ac.set_index('Date_Time').groupby(pd.Grouper(freq='H'))['C1'].mean()
diaC1 = horaC1.groupby(pd.Grouper(freq='D')).mean()
semanaC1 = diaC1.groupby(pd.Grouper(freq='W')).mean()
mesC1 = semanaC1.groupby(pd.Grouper(freq='M')).mean()

##C2
horaC2= data_ac.set_index('Date_Time').groupby(pd.Grouper(freq='H'))['C2'].mean()
diaC2 = horaC2.groupby(pd.Grouper(freq='D')).mean()
semanaC2 = diaC2.groupby(pd.Grouper(freq='W')).mean()
mesC2 = semanaC2.groupby(pd.Grouper(freq='M')).mean()

horaC3= data_ac.set_index('Date_Time').groupby(pd.Grouper(freq='H'))['C3'].mean()
diaC3 = horaC3.groupby(pd.Grouper(freq='D')).mean()
semanaC3 = diaC3.groupby(pd.Grouper(freq='W')).mean()
mesC3 = semanaC3.groupby(pd.Grouper(freq='M')).mean()

horaC4= data_ac.set_index('Date_Time').groupby(pd.Grouper(freq='H'))['C4'].mean()
diaC4 = horaC4.groupby(pd.Grouper(freq='D')).mean()
semanaC4 = diaC4.groupby(pd.Grouper(freq='W')).mean()
mesC4 = semanaC4.groupby(pd.Grouper(freq='M')).mean()

horaC5= data_ac.set_index('Date_Time').groupby(pd.Grouper(freq='H'))['C5'].mean()
diaC5 = horaC5.groupby(pd.Grouper(freq='D')).mean()
semanaC5 = diaC5.groupby(pd.Grouper(freq='W')).mean()
mesC5 = semanaC5.groupby(pd.Grouper(freq='M')).mean()

horaC6= data_ac.set_index('Date_Time').groupby(pd.Grouper(freq='H'))['C6'].mean()
diaC6 = horaC6.groupby(pd.Grouper(freq='D')).mean()
semanaC6 = diaC6.groupby(pd.Grouper(freq='W')).mean()
mesC6 = semanaC6.groupby(pd.Grouper(freq='M')).mean()
#
#GRAFICAS
semana=pd.DataFrame({'C1' : semanaC1, 'C2': semanaC2, 'C3': semanaC3,'C4' : semanaC4, 'C5': semanaC5, 'C6': semanaC6})
#mes = pd.DataFrame({'mV' : mesV, 'mR': mesR})
#mes = pd.DataFrame({'mV' : mesV, 'mB': mesB,'mC':mesC,'mE':mesE,'mM':mesM,'mR': mesR,'mS':mesS})
fig, ax = plt.subplots() 

#ax = semana.plot(kind='bar', title='GMM_MEX, Saw_Rum ',  fontsize=5,  align='center', width=0.9 )
#ax = mes.plot(kind='bar', title='Saw_Rum, Bc Stations ',  fontsize=5,  align='center', width=0.8 )
#ax=mes.plot.bar(width=0.9)
ax=semana.plot.bar(width=0.9)

ax.set(xlabel="Date",
       ylabel="Mean",
       title="Comparison between real data \n and those obtained by GMM in year 2010");


# Make most of the ticklabels empty so the labels don't get too crowded
#ticklabels = ['']*len(mesV.index)
ticklabels = ['']*len(semanaC1.index)
# Every 4th ticklable shows the month and day
ticklabels[::4] = [item.strftime('%b %d') for item in semanaC1.index[::4]]
#ticklabels[::5] = [item.strftime('%b %d') for item in mesV.index[::5]]
# Every 12th ticklabel includes the year
#ticklabels[::12] = [item.strftime('%b %d\n%Y') for item in mesV.index[::12]]
ticklabels[::52] = [item.strftime('%b %d\n%Y') for item in semanaC1.index[::52]]
ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
plt.gcf().autofmt_xdate()
plt.savefig("./Rumorosa_10.png",dpi=300,format="png") 
# plt.show()
