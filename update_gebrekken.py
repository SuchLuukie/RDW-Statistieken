import requests
import json


def writeJSON(filename, data):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)

def loadJSON(filename):
	with open(filename, "r") as json_file:
		return json.load(json_file)



gebrekken_nummers_link = "https://opendata.rdw.nl/resource/hx2c-gt7k.json"

alle_nummers = requests.get(gebrekken_nummers_link)
alle_nummers = alle_nummers.json()

library = {}
for nummer in alle_nummers:
	library.update({nummer["gebrek_identificatie"]: {"omschrijving": nummer["gebrek_omschrijving"]}})


writeJSON("gebrekken.json", library)