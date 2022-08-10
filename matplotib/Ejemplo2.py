# import section
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
from datetime import date
from itertools import product
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

# generate a dataframe like yours
#EJE X y EJEY
date = [date(2020, m, d).strftime("%B %d") for m, d in product(range(1, 13, 1), range(1, 29, 1))]
# print(date) # Dias pero uno por uno con su mes 
# print(len(date)) # Dias del año 336

value = np.abs(np.random.randn(len(date)))
# print(value) ##Valores aleatorios
data = pd.DataFrame({'date': date,
                     'value': value})
data.set_index('date', inplace = True)


# convert index from str to date
data.index = pd.to_datetime(data.index, format = '%B %d')

# prepare days and months axes
fig = plt.figure(figsize = (16, 8)) # Tamaño de la imagen
days = host_subplot(111, axes_class = AA.Axes, figure = fig)
plt.subplots_adjust(bottom = 0.1)
months = days.twiny()

# position months axis
# Meses
offset = -20
new_fixed_axis = months.get_grid_helper().new_fixed_axis
months.axis['bottom'] = new_fixed_axis(loc = 'bottom',
                                       axes = months,
                                       offset = (0, offset))
months.axis['bottom'].toggle(all = True)

#plot
#Barras
days.bar(data.index, data['value'])

# Mostrar los dias
# formatting days axis
days.xaxis.set_major_locator(md.DayLocator(interval = 10))
days.xaxis.set_major_formatter(md.DateFormatter('%d'))
plt.setp(days.xaxis.get_majorticklabels(), rotation = 0)
days.set_xlim([data.index[0], data.index[-1]])

# Mostrar los meses
# formatting months axis
months.xaxis.set_major_locator(md.MonthLocator())
months.xaxis.set_major_formatter(md.DateFormatter('%b'))
months.set_xlim([data.index[0], data.index[-1]])

plt.show()