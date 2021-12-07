from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import NMF
from vectorized_lemmatized_articles import vectorized_lemmatized_articles


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
c=[69,70,74,77,79,6,18,29,28,5]


arts_notime=articles[['title','summary']]
vla1=vectorized_lemmatized_articles(arts_notime,0,arts_notime.shape[0])
vektory = vla1.run()

vectorizer = TfidfVectorizer(max_features=900)
X = vectorizer.fit_transform(vektory)
nmf = NMF(n_components=10, random_state=42, alpha=0.1, l1_ratio=0.5).fit(X)
topic_to_articles=nmf.transform(X)
arts_cut=topic_to_articles[c,:]
avg=np.mean(arts_cut,axis=0)
cos=np.zeros(topic_to_articles.shape[0])
for i in range(topic_to_articles.shape[0]):
    cos[i]=cosine_similarity(topic_to_articles[i,:].reshape((1,-1)),avg.reshape((1,-1)))
cos90=cos.copy()
cos90[cos90<0.9]=0
cos70=cos.copy()
cos70[cos70>=0.9]=0
cos70[cos70<0.7]=0
cos50=cos.copy()
cos50[cos50>=0.7]=0
cos50[cos50<0.5]=0
cos10=cos.copy()
cos10[cos10>0.1]=0
index_90 = np.where(cos90!=0)
articles_90=articles.loc[index_90]
articles_90.sort_values(by=['published'])
rec_ind_90=articles_90[-3:].index
index_70 = np.where(cos70!=0)
articles_70=articles.loc[index_70]
articles_70.sort_values(by=['published'])
rec_ind_70=articles_70[-3:].index
index_50 = np.where(cos50!=0)
articles_50=articles.loc[index_50]
articles_50.sort_values(by=['published'])
rec_ind_50=articles_50[-3:].index
index_10 = np.where(cos10!=0)
articles_10=articles.loc[index_10]
articles_10.sort_values(by=['published'])
rec_ind_10=articles_10[-1:].index

rec_ind=np.concatenate((rec_ind_90,rec_ind_70,rec_ind_50,rec_ind_10))


