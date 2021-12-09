from persona import persona
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate
import pandas as pd
import numpy as np
import csv



def csv2dict():
    file = open("../data/article_archive.csv", encoding="utf-8")
    csvreader = csv.reader(file)
    header = next(csvreader)
    zpravy_csv = []
    for row in csvreader:
        zpravy_csv.append(row)
    file.close()

    pom = zpravy_csv[0]   

    zpravy = [
        {'id': 0, header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]}
            ]   

    for i in range(1,np.size(zpravy_csv,0)):
        pom = zpravy_csv[i]
        zpravy.append({'id': i, header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]})
    
    return zpravy

def vyber_zpravy(pocet, kategorie):
    zpravy = csv2dict()
    articles_all = pd.DataFrame(zpravy)
    articles_sort = articles_all.sort_values(by=['published'], ascending=False)

    articles2 = []
    velikost = 0
    k = 0

    while velikost <= pocet-1:
        if kategorie == 'all':
            articles_kategorie = articles_sort
        else:
            articles_kategorie = articles_sort[articles_sort['category'] == kategorie]
        articles=articles_kategorie.iloc[:pocet+k,[1,3]]
        vla=vectorized_lemmatized_articles(articles,0,articles.shape[0])
        ded=deduplicate(vla.run())
        b=ded.run()
        if len(b) != 0:
            articles2 = articles.drop(articles.index[b])
        else:
            articles2=articles

        ind_pom = articles2.index
        velikost = articles2.shape[0]
        k = k + 1

    zpravy_vybrane = articles_all.iloc[ind_pom].to_dict('records')
    return zpravy_vybrane

def personalizovane_zpravy(jmeno_uzivatele):
    zpravy = csv2dict()
    zpravy_all = pd.DataFrame(zpravy)
    jmeno = jmeno_uzivatele
    seznam = pd.read_csv("../data/likes.csv")
    kliknute_indexy = seznam.loc[seznam['user'] == jmeno]['zprava_id'].to_numpy()
    if len(kliknute_indexy)<5:
        return 'klikni alespoň na 5 článků!'
    else:
        vybrane_indexy_mod = persona(zpravy_all,kliknute_indexy)
        vybrane_indexy = vybrane_indexy_mod.run()
        
        zpravy_vybrane = zpravy_all.iloc[vybrane_indexy].to_dict('records')
        
        return zpravy_vybrane

vyber = personalizovane_zpravy('jan_von_trodler')
vyber2 = pd.DataFrame(vyber)
    
    
    
    
    