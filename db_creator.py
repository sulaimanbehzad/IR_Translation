from tinydb import TinyDB, Query
import pandas as pd

db = TinyDB('db.json')
columns = ['ID', 'POS', 'Gloss']
afterTranslation = ['ID', 'POS', 'Gloss', 'Gloss_persian', 'Checked']
fileds = pd.read_csv('10.csv', header=None, names=columns)
fileds = fileds.iloc[1:]
list = fileds.values.tolist()
for i in list:
    temp = {
        'ID': i[0],
        'POS': i[1],
        'Gloss': i[2],
        'Gloss_persian': '',
        'Checked': 0
    }
    db.insert(temp)
