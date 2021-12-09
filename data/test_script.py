import pandas as pd
import numpy as np
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate

#df=pd.ExcelFile('../data/article_archive2.csv')
df=pd.read_csv ('../data/article_archive2.csv')
#articles=df.parse('article_archive')
#c=np.array([5546,5542,5540,5470,5483,5490,5493,5501,5477,5495,5505,5476])
articles=df
#articles=articles[['title','summary']]

vla=vectorized_lemmatized_articles(articles,0,articles.shape[0])
a=vla.run()
ded=deduplicate(a)
b=ded.run()

