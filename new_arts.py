import pandas as pd
import numpy as np

df1=pd.read_csv ('data/article_archive_14_12_all_time.csv')
df2=pd.read_csv ('data/article_archive_allnew_cat_time.csv')
# df3=pd.read_csv ('data/article_archive_I7_12.csv')
# df4=pd.read_csv ('data/article_archive_I9_12.csv')
# df5=pd.read_csv ('data/article_archive_idnes9_12.csv')
# df6=pd.read_csv ('data/article_archive_lid9_12.csv')
# df7=pd.read_csv ('data/article_archive2.csv')

# frames= [df5,df6,df7]
frames = [df1,df2]#,df3,df4]#[df5,df6,df7]
result = pd.concat(frames)
result=result.reset_index()
result=result.drop(columns='index')
a=np.where(result['title']=='title')
a=np.array(a)
a=a[0,:]
df=result.drop(result.index[a])
df=df.iloc[:,0:7]
#df.insert(1, 'photo', np.zeros(df.shape[0]))

ir='https://getvectorlogo.com/wp-content/uploads/2019/11/irozhlas-vector-logo.png'
dn='https://static.novydenik.com/2020/09/logo_denikn_rgb.png'
for i in range(df.shape[0]):
    if df.iloc[i,6]=='denikn.cz':
        df.iloc[i,1]=dn
    elif df.iloc[i,6]=='irozhlas.cz':
        df.iloc[i,1]=ir
df.insert(0,'id',np.linspace(0,df.shape[0]-1,df.shape[0]))

df.to_csv('data/article_archive_final.csv',index=False, header=df.columns, mode='a')

### FIN UPRAVY
# import pandas as pd
# df=pd.read_csv ('data/article_archive_allnew.csv')
# #df['category'] = df['category'].astype('category')
# for i in range(df.shape[0]):
#     if df.iloc[i,6]=='Události - Názory':
#         df.iloc[i,6]='Ostatní'
#     elif df.iloc[i,6]=='mix':
#         df.iloc[i,6]='Ostatní'
#     elif df.iloc[i,6]=='Události - Briefing':
#         df.iloc[i,6]='Ostatní'
#     elif df.iloc[i,6]=='OnaDnes - Vztahy':
#         df.iloc[i,6]='Ostatní'
#     elif df.iloc[i,6]=='Auto':
#         df.iloc[i,6]='Ostatní'
#     elif df.iloc[i,6]=='Cestování':
#         df.iloc[i,6]='Ostatní'
#     elif df.iloc[i,6]=='Revue - Společnost':
#         df.iloc[i,6]='Ostatní'
        
# df.to_csv('data/article_archive_allnew_cat.csv',index=False, header=df.columns, mode='a')
