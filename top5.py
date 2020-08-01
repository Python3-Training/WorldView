#!/usr/bin/env python3
''' (obsolete) Top 5: Cobbling together the official 
pic for the month as a manual process.'''

# Archive Notes:
# -------------
# Graphical compsoition remains in local facebook "Data" archive.
# Historical data artifacts uploaded from same to:
# https://github.com/Python3-Training/WorldView

import matplotlib.pyplot as plt
from collections import OrderedDict

zData = OrderedDict()
zData['ASIA'] = 3191
zData['INDIA'] = 3848
zData['AMERICAS'] = 877+577
zData['AFRICA'] = 2213
zData['EUROPE'] = 1488

zData = OrderedDict(sorted(zData.items(), key=lambda a: a[1]))

labels = zData.keys()
sizes =  zData.values()

explode = (0.2, 0, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal') 
plt.show()
