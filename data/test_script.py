import pandas as pd
import numpy as np
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate

df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Github/01DASteam/data/article_archive_cleared.xls')
articles=df.parse('article_archive')
c=np.array([5546,5542,5540,5470,5483,5490,5493,5501,5477,5495,5505,5476])
articles=articles.loc[c,['title','summary']]
#articles=articles[['title','summary']]

vla=vectorized_lemmatized_articles(articles,0,articles.shape[0])
ded=deduplicate(vla.run())
b=ded.run()

