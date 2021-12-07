import pandas as pd
import numpy as np
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate
from persona import persona
import csv
def csv2dict():
    file = open("article_archive.csv", encoding="utf8")
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

zpravy = csv2dict()
articles = pd.DataFrame(zpravy)

articles=articles[['title','summary','published']]
c=[69,70,74,77,79]#,6,18]#29,28,5]
per=persona(articles,c)
aaaa=per.run()
