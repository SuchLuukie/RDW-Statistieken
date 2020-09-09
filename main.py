# libraries
from more_itertools import sort_together
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

def writeJSON(filename, data):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)

def loadJSON(filename):
	with open(filename, "r") as json_file:
		return json.load(json_file)

data = loadJSON("afgekeurde_voortuigen.json")
#gebrekken = loadJSON("gebrekken.json")

name = []
length = []
for a in data:
	if len(data[a]) > 200:
		name.append(a)
		length.append(len(data[a]))

values = sort_together([length, name], reverse=True)

x = np.arange(len(values[0]))

fig, ax = plt.subplots()

ax.bar(values[1], values[0])

ax.set_xticks(x)
ax.set_xticklabels(values[1], rotation = (45))

plt.show()