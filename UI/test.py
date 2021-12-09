import pandas as pd
import csv
import numpy as np
from persona import persona

def like(name, id):
    data = {}
    data.setdefault('user', [])
    data.setdefault('zprava_id', [])
    data['user'].append(name)
    data['zprava_id'].append(id)
    df = pd.DataFrame(data)
    df.to_csv('../data/likes_posted.csv',index=False, header=False, mode='a')


def csv2dict():
    file = open("../data/article_archive.csv", encoding='utf8')
    csvreader = csv.reader(file)
    header = next(csvreader)
    zpravy_csv = []
    for row in csvreader:
        zpravy_csv.append(row)
    file.close()

    pom = zpravy_csv[0]

    zpravy = [
        {'id': 0, header[1]: pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5],
         header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]}
    ]

    for i in range(1, np.size(zpravy_csv, 0)):
        pom = zpravy_csv[i]
        zpravy.append(
            {'id': i, header[1]: pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5],
             header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]})

    return zpravy

def personalizovane_zpravy(jmeno_uzivatele):
    zpravy = csv2dict()
    zpravy_all = pd.DataFrame(zpravy)
    zpravy_all.loc[zpravy_all['category'] == 'Zprávy z domova', 'category'] = 'Domov'
    zpravy_all.loc[zpravy_all['category'] == 'Zprávy ze světa', 'category'] = 'Svět'
    zpravy_all.loc[zpravy_all['category'] == 'Byznys zprávy', 'category'] = 'Ekonomika'
    zpravy_all.loc[zpravy_all['category'] == 'Zajímavosti', 'category'] = 'Životní styl'
    zpravy_all.loc[zpravy_all['category'] == 'Životní styl a společnost', 'category'] = 'Životní styl'
    zpravy_all.loc[zpravy_all['category'].str.contains('Věda a technologie'), 'category'] = 'Věda'
    zpravy_all.loc[zpravy_all['category'] == 'Česko', 'category'] = 'Domov'
    jmeno = jmeno_uzivatele
    seznam = pd.read_csv("../data/likes.csv")
    kliknute_indexy = seznam.loc[seznam['user'] == jmeno]['zprava_id'].to_numpy()
    if len(kliknute_indexy) < 5:
        return 'klikni alespoň na 5 článků!'
    else:
        vybrane_indexy_mod = persona(zpravy_all, kliknute_indexy)
        vybrane_indexy = vybrane_indexy_mod.run()

        zpravy_vybrane = zpravy_all.iloc[vybrane_indexy].to_dict('records')

        return zpravy_vybrane

z = personalizovane_zpravy('buracek')
print(z[3]['source'])
