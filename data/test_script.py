import pandas as pd
import numpy as np
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate

df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Github/01DASteam/data/article_archive_cleared.xls')
articles=df.parse('article_archive')
c=np.array([0,1,2,441,443,314,307,306,7,10])
articles=articles.loc[c,['title','summary']]

vla=vectorized_lemmatized_articles(articles,0,articles.shape[0])
ded=deduplicate(vla.run())
b=ded.run()

