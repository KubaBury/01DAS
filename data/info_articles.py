import pandas as pd
import numpy as np
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate

#df=pd.ExcelFile('../data/article_archive2.csv')
df=pd.read_csv ('../data/article_archive4.csv')
dg=df
#articles=df.parse('article_archive')
#c=np.array([5546,5542,5540,5470,5483,5490,5493,5501,5477,5495,5505,5476])
articles=df
#articles=articles[['title','summary']]

vla=vectorized_lemmatized_articles(articles,0,articles.shape[0])
a=vla.run()
ded=deduplicate(a)
b=ded.run()
df = df.rename(columns={'Na světové scéně se odehrávají tři potenciální krize': 'title', '<img src="https://infocz-media.s3.amazonaws.com/infocz/production/files/2021/12/07/10/41/19/218b499d-7361-403e-8df9-df0d6dd91f95/profimedia-0646255968.jpg" /> Možná ruská invaze na Ukrajinu, čínský tlak na Tchaj-wan a chatrná jednání o íránském jaderném programu představují pro amerického prezidenta Joea Bidena nebezpečný okamžik.': 'summary','Tue, 07 Dec 2021 11:30:00 +0100':'published','https://www.info.cz/wall-street-journal/na-svetove-scene-se-odehravaji-tri-potencialni-krize':'link','lidovky.cz':'source'})
articles=df
articles['photo']=articles.iloc[:,1]
for i in range(len(articles)):
    if articles.iloc[i,5].find('.png')==-1:
        articles.loc[i,'photo']=dg.iloc[i,1][dg.iloc[i,1].find('"')+1:dg.iloc[i,1].find('.jpg')+4]
    elif articles.iloc[i,5].find('.jpg')==-1:
        articles.loc[i,'photo']=dg.iloc[i,1][dg.iloc[i,1].find('"')+1:dg.iloc[i,1].find('.png')+4]
    articles.loc[i,'summary']=dg.iloc[i,1][dg.iloc[i,1].find('/>')+2:]

columns=['title','summary','published','link','source','photo']
articles.to_csv('article_archive_info.csv',index=False, header=columns, mode='a')
    





