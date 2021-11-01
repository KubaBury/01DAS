from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate
import pandas as pd
import numpy as np
import csv


def csv2dict():
    file = open("/home/jan/Documents/DAS/01DAS/data/article_archive.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    zpravy_csv = []
    for row in csvreader:
        zpravy_csv.append(row)
    file.close()

    pom = zpravy_csv[0]   

    zpravy = [
        {'id': pom[0], header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]}
            ]   

    for i in range(1,np.size(zpravy_csv,0)):
        pom = zpravy_csv[i]
        zpravy.append({'id': pom[0], header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]})
    
    return zpravy

def vyber_zpravy():

    zpravy = csv2dict()
    articles_all = pd.DataFrame(zpravy)
    
    #c=np.array([0,1,2,443,314,307,306,7,10])
    #c = np.arange(0,10)
    #c = np.arange(300,310)
    #c = np.arange(0,10)
    
    #articles=articles_all.iloc[c,[1,3]]
    
    articles2 = []
    k = 0
    velikost = 0
    
    while velikost <= 14:
        c = c = np.arange(300,315 + k)    
        articles=articles_all.iloc[c,[1,3]]    
        vla=vectorized_lemmatized_articles(articles,0,c.shape[0])
        ded=deduplicate(vla.run())
        b=ded.run()
        if len(b) != 0:
            bb = [x+300 for x in b]
            articles2 = articles.drop(bb)
        
        velikost = articles2.shape[0]
        k = k + 1
    
    zpravy_vybrane = articles2.to_dict('records')
    return zpravy_vybrane

