import pandas as pd

afterTranslation = ['ID', 'POS', 'Gloss', 'Gloss_persian', 'Checked']
df = pd.read_json('db.json')
final = df.values.tolist()
list = []
for item in final:
    dict = item[0]
    temp = []
    temp.append(dict['ID'])
    temp.append(dict['POS'])
    temp.append(dict['Gloss'])
    temp.append(dict['Gloss_persian'])
    temp.append(dict['Checked'])
    list.append(temp)
df = pd.DataFrame(list, columns=afterTranslation)
df.to_csv('translatedCSV.csv', index=False, encoding='utf-8-sig')
