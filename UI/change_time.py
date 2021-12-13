import pandas as pd
from datetime import datetime
df=pd.read_csv('../data/article_archive_allnew_cat.csv')
df['category'] = df['category'].astype('category')
for i in range(df.shape[0]):
    df.iloc[i,4]=df.iloc[i,4][5:25]
    day=df.iloc[i,4][0:2]
    month=df.iloc[i,4][3:6]
    year=df.iloc[i,4][9:11]
    hour=df.iloc[i,4][12:20]
    if month=='Dec':
        month='12'
    elif month=='Nov':
        month='11'
    df.iloc[i,4]=str(month+'/'+day+'/'+year+' '+hour)
df.to_csv('../data/article_archive_allnew_cat_time.csv',index=False, header=df.columns, mode='a')