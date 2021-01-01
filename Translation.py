import pandas as pd
from google_trans_new import google_translator
from tinydb import TinyDB, Query


begin = 17838
end = 17839
db = TinyDB('db.json')
user = Query()
translator = google_translator()
id = begin
while id < end:
    temp = db.search(user.ID == str(id))[0]
    db.upsert({'Gloss_persian': translator.translate(temp['Gloss'], lang_src='english', lang_tgt='fa')},
              user.ID == str(id))
    temp = db.search(user.ID == str(id))[0]
    print(temp['Gloss_persian'])
    id += 1
# columns = ['ID', 'POS', 'Gloss']
# afterTranslation = ['ID', 'POS', 'Gloss', 'Gloss_persian', 'Checked']
# fileds = pd.read_csv('12.csv', header=None, names=columns)
# fileds = fileds.iloc[1:]
# list = fileds.values.tolist()
# persian = []
# checked = []
# for i in list:
#     checked.append(0)
# translator = google_translator()
# for items in list:
#     result = translator.translate(items[2], lang_src='english', lang_tgt='fa')
#     persian.append(result)
#     print(result)
# final = []
# i = 0
# for items in list:
#     temp = []
#     temp.append(items[0])
#     temp.append(items[1])
#     temp.append(items[2])
#     temp.append(persian[i])
#     temp.append(checked[i])
#     i = i + 1
#     final.append(temp)
# df = pd.DataFrame(final, columns=afterTranslation)
# df.to_csv('translatedCSV.csv', index=False, encoding='utf-8-sig')
