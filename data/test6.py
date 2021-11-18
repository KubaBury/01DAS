import pandas as pd
import numpy as np
import random
from vectorized_lemmatized_articles2 import vectorized_lemmatized_articles2
from deduplicate2 import deduplicate2

df=pd.read_csv('datatest.csv',delimiter=',')  

a=np.array(df.columns)
b=np.zeros(a.shape)
c=np.zeros(a.shape)
for i in range(len(a)):
    c[i] = a[i][0:5]
    b[i]= c[i]*pow(10,int(a[i][23]))

data=np.array([b,df.iloc[0]])

def Rand(start, end, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start, end))
 
    return res
 
num = 50
start = 0
end = 27627
ind1=Rand(start, end, num)
duplicates=data[:,ind1]
ind2=Rand(0, 5548, 200)

df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Github/01DASteam/data/article_archive_cleared.xls')
articles=df.parse('article_archive')
articles=articles[['title','summary']]
vla=vectorized_lemmatized_articles2(articles,ind2)
ded=deduplicate2(vla.run())
notduplicates=ded.run()
ind3=Rand(0, len(notduplicates[0])-1, 50)

nd=np.zeros((2,50))
for i in range(len(ind3)):
    nd[0,i]=notduplicates[0][ind3[i]]
    nd[1,i]=notduplicates[1][ind3[i]]

nda=np.zeros((50))
for i in range(len(ind3)):
    if nd[0,i]==nd[1,i]:
        nda[i]=1
    else:
        nda[i]=0
        
ddd=articles
for type in ddd.columns:
    ddd[type]=ddd[type].astype(str)

data=[]
for i in range(ddd.shape[0]):
    g=' '.join(ddd.iloc[i])
    data.append(g)
        
darts=[]
arts=[]
for i in range(len(ind2)):
    arts.append(data[ind2[i]])
narts=[]
for i in range(len(ind3)):
    g=[]
    g.append(data[int(duplicates[0,i])])
    g.append(data[int(duplicates[1,i])])
    darts.append(g)
    h=[]
    h.append(arts[int(nd[0,i])])
    h.append(arts[int(nd[1,i])])
    narts.append(h)