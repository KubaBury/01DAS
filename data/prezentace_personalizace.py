from persona import persona
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate
import pandas as pd
import numpy as np
import csv



def csv2dict():
    file = open("../data/article_archive_allnew_cat_time.csv", encoding='utf8')
    csvreader = csv.reader(file)
    header = next(csvreader)
    zpravy_csv = []
    for row in csvreader:
        zpravy_csv.append(row)
    file.close()

    pom = zpravy_csv[0]

    zpravy = [{'id': 0, header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7]}]

    for i in range(1, np.size(zpravy_csv, 0)):
        pom = zpravy_csv[i]
        zpravy.append({'id': i, header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7]})

    return zpravy


zpravy = csv2dict()
zpravy_all = pd.DataFrame(zpravy)
zpravy_all.loc[zpravy_all['category'] == 'Zprávy z domova', 'category'] = 'Domov'
zpravy_all.loc[zpravy_all['category'] == 'Zprávy ze světa', 'category'] = 'Svět'
zpravy_all.loc[zpravy_all['category'] == 'Byznys zprávy', 'category'] = 'Ekonomika'
zpravy_all.loc[zpravy_all['category'] == 'Zajímavosti', 'category'] = 'Životní styl'
zpravy_all.loc[zpravy_all['category'] == 'Životní styl a společnost', 'category'] = 'Životní styl'
zpravy_all.loc[zpravy_all['category'].str.contains('Věda a technologie'), 'category'] = 'Věda'
zpravy_all.loc[zpravy_all['category'] == 'Česko', 'category'] = 'Domov'

jmeno = 'jan_von_trodler'

seznam = pd.read_csv("../data/likes.csv")
#kliknute_indexy = seznam.loc[seznam['user'] == jmeno]['zprava_id'].to_numpy()
#kliknute_indexy = [48,49,127,194,221,223]
kliknute_indexy = [44,52,79,158,231]
kliknute_zpravy = zpravy_all.loc[kliknute_indexy]
if len(kliknute_indexy)<5:
    print('klikni alespoň na 5 článků!')
else:
    vybrane_indexy_mod = persona(zpravy_all,kliknute_indexy)
    vybrane_indexy = vybrane_indexy_mod.run()
    
    zpravy_vybrane = zpravy_all.iloc[vybrane_indexy].to_dict('records')
    

vyber = pd.DataFrame(zpravy_vybrane)
    

    
    