import csv
import json
import pandas as pd

df = pd.read_csv('cannabis.csv')

print(df.head())

df['Effects'] = df['Effects'].str.split(',')
df['Flavor'] = df['Flavor'].str.split(',')

df.to_csv('data.csv', index=False)

csvfile = open('data.csv', 'r')
jsonfile = open('cannabis.json', 'w')

fieldnames = ('Strain','Type','Rating','Effects','Flavor','Description')
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)