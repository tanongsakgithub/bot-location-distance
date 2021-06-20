import pandas
import json
import genflex
import Filetools
from geopy.distance import great_circle

def myFunc(e):
  return e['distance']
def calculate(latitude,longitude):
	mylocation = (latitude,longitude)
	datasheet = Filetools.get_datasheet()
	result = []
	count = 0
	for row in datasheet:
		count += 1
		cleveland_oh = (row["latitude"], row["longitude"])
		distanceresult  = great_circle(mylocation, cleveland_oh).km
		jsonobj = {'distance': round(distanceresult, 2)}
		row.update(jsonobj)
		result.append(row)
		if(count >= 12):
			break
	result.sort(key=myFunc)
	return result
