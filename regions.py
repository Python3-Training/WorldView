#!/usr/bin/env python3
''' Mission: Assign, tally & chart a regional aggregation 
for every country, as seen in the Facebook-reported 
country collection. 
'''
from collections import OrderedDict

fregions = "./stats/regions.tdf"
fmembers = "./stats/members.tdf"

print("\nRegional Assignments:\n")
regions = dict()
with open(fregions) as fh:
    for line in fh:
        line = line.strip()
        cols = line.split('\t')
        if len(cols) is not 2:
            print("Error")
            continue
        regions[cols[0].upper()] = cols[1].upper()

geek_zones = dict()
for key in regions:
    region = regions[key]
    if not region in geek_zones:
        geek_zones[region] = list()
    geek_zones[region].append(key)

for ss, key in enumerate(geek_zones, 1):
    print(f'Zone {ss}: "{key}"')
    for country in sorted(geek_zones[key]):
        print(f"\t{country}")

print("\n\nRegional Stats:\n")
calcs = dict()
with open(fmembers) as fh:
    for line in fh:
        cols = line.strip().split("\t")
        if len(cols) is not 2:
            print("ERror2")
            continue
        country = cols[0].upper()
        if country not in regions:
            print(f"Error: {cols[0]} not in regions.")
            continue
        count = int(cols[1].strip())
        region = regions[country]
        if region not in calcs:
            calcs[region] = count
        else:
            calcs[region] += count

labels = list()
sizes = list()
ranks = sorted(calcs, key=lambda a:calcs[a])
for key in ranks:
    print(f"{key:10}{calcs[key]}")
    labels.append(key)
    sizes.append(calcs[key])

import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
plt.title("Python3 Training", loc="Right")
plt.show()


print("\n\n\n(end)")
    




