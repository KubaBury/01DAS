import pandas as pd
import numpy as np

from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate2 import deduplicate2


df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Github/01DASteam/data/article_archive_cleared.xls')
articles=df.parse('article_archive')
wtf=np.linspace(0,5547,5548)
wtf=wtf.astype('int32')
articles['ID']=wtf
#articles=articles.insert(0, 'ID', range(0, 0 + len(articles)))
articles=articles[['title','summary','ID']]


#articles['category']=articles['category'].astype('category')


a1=np.linspace(0, 29,30)
a2=np.linspace(300,319,20)
a3=np.linspace(440,449,10)
a=np.concatenate([a1,a2,a3])
#b=np.array([496,497,498,499,500,521,522,523,524,536,537,538,542,543,544,551,559,562,564,577,586,589,590,591,592,593,607,608,609,610,611,612,626,627,630,638,641,646,647,656,664,671,683,684,685,686,687])
#c=np.concatenate([a,b])
articles_find=articles.loc[a]

vla=vectorized_lemmatized_articles(articles_find,0,449)
ded=deduplicate2(vla.run())
bb=ded.run()