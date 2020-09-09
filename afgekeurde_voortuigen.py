import requests
import json

def writeJSON(filename, data):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)

def loadJSON(filename):
	with open(filename, "r") as json_file:
		return json.load(json_file)


alle_afgekeurde_autos = requests.get("https://opendata.rdw.nl/resource/7gdq-njxy.json?$limit=50000").json()
gebrekken = loadJSON("gebrekken.json")

dictio = {}
for gebrek in gebrekken:
	dictio.update({gebrek: []})

for auto in alle_afgekeurde_autos:
	dictio[auto["gebrek_identificatie"]].append(auto)

writeJSON("afgekeurde_voortuigen.json", dictio)
