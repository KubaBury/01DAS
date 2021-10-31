from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate
import pandas as pd
import numpy as np

df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Audiozprávy/article_archive_cleared.xls')
articles=df.parse('article_archive')
#c=np.array([0,1,2,3,4,5,6,7,441,442,443,444,445,446,447])
c=np.array([0,1,2,443,314,307,306,7,10])
articles=articles.iloc[c,[0,2]]

vla=vectorized_lemmatized_articles(articles,0,c.shape[0])
ded=deduplicate(vla.run())
b=ded.run()