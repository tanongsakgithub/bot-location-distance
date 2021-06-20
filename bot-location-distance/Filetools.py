import pandas
import json
import os
#sheetid = os.environ['SHEET_ID']
#sheetname = os.environ['SHEET_NAME']
sheetid = "1c0Es1glnAT3cR4GA1b2eiDJMBOs7_tlaZpxj-z3h5HU"
sheetname = "Catalog"
def get_datasheet():
	df = pandas.read_csv('https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(sheetid,sheetname))
	data = df.to_json(orient="records")
	parsed = json.loads(data)
	return parsed