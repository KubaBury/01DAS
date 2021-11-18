import pandas as pd
import numpy as np


df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Github/01DASteam/data/article_archive_cleared.xls')
articles=df.parse('article_archive')
#articles=articles[['title','summary']]
articles['category']=articles['category'].astype('category')
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
###main

articles2=articles.loc[duplicates_inds[0,:]]
articles2['article2']=articles2['title']+ ' '+articles2['summary']
articles3=articles.loc[duplicates_inds[1,:]]
articles3['article3']=articles3['title']+ ' '+articles3['summary']
dh={'articles1': articles2['article2'],'articles2': articles3['article3'],'isduplicate': duplicates_inds[2,:]}
b=np.array([dh['articles1'],dh['articles2'],dh['isduplicate']])
b=b.transpose()
art_fin=pd.DataFrame(data=b)
art_fin=art_fin.rename(columns={2: "is_duplicate"})

###############

from vectorized_lemmatized_articlesXGB import vectorized_lemmatized_articlesXGB

from sklearn.feature_extraction.text import TfidfVectorizer
import scipy

vectorizer = TfidfVectorizer(ngram_range=(1,2))


vla=vectorized_lemmatized_articlesXGB(art_fin[0], 0, art_fin.shape[0])
x1=vla.run()
vla2=vectorized_lemmatized_articlesXGB(art_fin[1], 0, art_fin.shape[0])
x2=vla2.run()
x=np.concatenate((x1,x2))


vectorizer.fit(x)

train1 = vectorizer.transform(x1)
train2 = vectorizer.transform(x2)

########
from sklearn.metrics.pairwise import cosine_similarity,cosine_distances
from sklearn.tree import DecisionTreeClassifier
########
cos_sim=np.zeros((train1.shape[0],1))
for i in range(train1.shape[0]):
    cos_sim[i]=cosine_similarity(train1[i],train2[i])
    

X=cos_sim
y = art_fin['is_duplicate']
y=y.astype('int')

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score
X_train,X_valid,y_train,y_valid = train_test_split(X,y, test_size = 0.33, random_state = 42)
clf = DecisionTreeClassifier()

clf.fit(X_train,y_train) 
pred=clf.predict(X_valid)
c=confusion_matrix(y_valid,pred)
p=precision_score(y_valid,pred)
r=recall_score(y_valid,pred)

#####
#train fin model
fin_model = DecisionTreeClassifier()
fin_model.fit(X,y) 
pred1=fin_model.predict(X)
pred2=fin_model.predict(X_valid)
pred3=fin_model.predict(X_train)

c1=confusion_matrix(y,pred1)
c2=confusion_matrix(y_valid,pred2)
c3=confusion_matrix(y_train,pred3)

import pickle
with open('fin_model.pickle', 'wb') as f:
    pickle.dump(fin_model, f)
    
# with open('fin_model.pickle', 'rb') as f:
#     fin_model = pickle.load(f)
# type(fin_model)

