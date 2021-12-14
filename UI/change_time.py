import pandas as pd
from datetime import datetime
df=pd.read_csv('../data/article_archive_14_12_all.csv')
#df['category'] = df['category'].astype('category')
for i in range(df.shape[0]):
    df.iloc[i,3]=df.iloc[i,3][5:25]
    day=df.iloc[i,3][0:2]
    month=df.iloc[i,3][3:6]
    year=df.iloc[i,3][9:11]
    hour=df.iloc[i,3][12:20]
    if month=='Dec':
        month='12'
    elif month=='Nov':
        month='11'
    df.iloc[i,3]=str(month+'/'+day+'/'+year+' '+hour)
df.to_csv('../data/article_archive_14_12_all_time.csv',index=False, header=df.columns, mode='a')