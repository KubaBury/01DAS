
from sklearn.metrics.pairwise import cosine_similarity,cosine_distances
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy

from vectorized_lemmatized_articlesXGB import vectorized_lemmatized_articlesXGB

import pandas as pd
import numpy as np

from datetime import datetime
start = datetime.now()

df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Github/01DASteam/data/article_archive_cleared.xls')
articles=df.parse('article_archive')
#articles=articles[['title','summary']]
articles['category']=articles['category'].astype('category')

#duplicates_inds=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,3,8,18,19,20],[1,3,8,9,10,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,29,441,446,303,305,316,312,308],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]])
#duplicates_inds=np.array([[1,5,3,8,18,19,20],[441,446,303,305,316,312,308],[1,1,1,1,1,1,1]])
#articles.loc[duplicates_inds[0,:],['title','summary']]
duplicates_inds = np.load('bb_final.npy')
a=np.concatenate([np.linspace(0, 29,30),np.linspace(300,319,20),np.linspace(440,449,10)])

aa=[(x,y) for x in a for y in a]
aa=np.array(aa)
indexy=[]
for i in range(aa.shape[0]):
    aa[i].sort()
    if aa[i,0]==aa[i,1]:
        indexy.append(i)
aa=np.delete(aa,indexy,0)
aa=np.unique(aa, axis=0)    
aa=aa.transpose()

aaa=np.array([[aa[0,:]],[aa[1,:]],[np.zeros(aa.shape[1])]])
aaa=aaa[:,0,:]

for i in range(duplicates_inds.shape[1]):
    duplicates_inds[0:2,i].sort()

for j in range(aaa.shape[1]):
    for i in range(duplicates_inds.shape[1]):
        if aaa[0,j]==duplicates_inds[0,i]:
            if aaa[1,j]==duplicates_inds[1,i]:
                aaa[2,j]=duplicates_inds[2,i]

duplicates_inds=aaa


articles2=articles.loc[duplicates_inds[0,:]]
articles2['article2']=articles2['title']+ ' '+articles2['summary']
articles3=articles.loc[duplicates_inds[1,:]]
articles3['article3']=articles3['title']+ ' '+articles3['summary']
dh={'articles1': articles2['article2'],'articles2': articles3['article3'],'isduplicate': duplicates_inds[2,:]}
b=np.array([dh['articles1'],dh['articles2'],dh['isduplicate']])
b=b.transpose()
art_fin=pd.DataFrame(data=b)
art_fin=art_fin.rename(columns={2: "is_duplicate"})


ind1=[1,2,3,4,5,6,7,8,9]
ind2=[1,2,3,4,5,6,7,8,9,10]
#cs=np.zeros((2,2,18))
ps=np.zeros((len(ind1),len(ind2)))
rs=np.zeros((len(ind1),len(ind2)))
for i in ind1:
    
    for j in ind2:
        if i< j:
            vectorizer1 = TfidfVectorizer(ngram_range=(i,j))
            
            
            vla=vectorized_lemmatized_articlesXGB(art_fin[0], 0, art_fin.shape[0])
            x1=vla.run()
            vla2=vectorized_lemmatized_articlesXGB(art_fin[1], 0, art_fin.shape[0])
            x2=vla2.run()
            x=np.concatenate((x1,x2))
            
            
            vectorizer1.fit(x)
            
            train1 = vectorizer1.transform(x1)
            train2 = vectorizer1.transform(x2)
            
            cos_sim=np.zeros((train1.shape[0],1))
            for k in range(train1.shape[0]):
                cos_sim[k]=cosine_similarity(train1[k],train2[k
                                                              ])
                
            
            X=cos_sim
            y = art_fin['is_duplicate']
            y=y.astype('int')
            
            X_train,X_valid,y_train,y_valid = train_test_split(X,y, test_size = 0.33, random_state = 42)
            clf1 = DecisionTreeClassifier()
            
            clf1.fit(X_train,y_train) 
            pred=clf1.predict(X_valid)
            c1=confusion_matrix(y_valid,pred)
            p1=precision_score(y_valid,pred)
            r1=recall_score(y_valid,pred)
            ps[i-1,j-1]=p1
            rs[i-1,j-1]=r1