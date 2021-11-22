from vectorized_lemmatized_articles import vectorized_lemmatized_articles
import pandas as pd
import numpy as np


#df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Audiozprávy/article_archive_cleared.xls')
#articles=df.parse('article_archive')
#articles=articles[['title','summary']]

#vla=vectorized_lemmatized_articles(articles,10)
#vektory=vla.run()

class deduplicate2:
    def __init__(self,vektory):
        self.vektory = vektory
        self.indexy_duplikatu= None
        
    def run(self):
        from sklearn.metrics.pairwise import cosine_similarity,cosine_distances
        a=np.zeros([self.vektory.shape[0],self.vektory.shape[0]])
        for i in range(a.shape[0]):
            for j in range(a.shape[0]):
                if j >= i:
                    break
                else:
                    a[i,j]=cosine_similarity(self.vektory[i],self.vektory[j])
        self.indexy_duplikatu=np.where(a>0.14)
        return self.indexy_duplikatu