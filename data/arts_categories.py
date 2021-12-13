import pandas as pd
import numpy as np
import csv
df=pd.read_csv ('article_archive_all_9_12_10am.csv')




for i in range(df.shape[0]):
    if df.iloc[i,5]=='Životní styl a společnost':
        df.iloc[i,5]='Životní styl'
    elif df.iloc[i,5]=='Věda a technologie':
        df.iloc[i,5]='Věda'
    elif df.iloc[i,5]=='Zprávy ze světa':
        df.iloc[i,5]='Svět'
    elif df.iloc[i,5]=='Zprávy z domova':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Česko':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Události - Domov':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Události - Svět':
        df.iloc[i,5]='Svět'
    elif df.iloc[i,5]=='Události - Byznys':
        df.iloc[i,5]='Ekonomika'
    elif df.iloc[i,5]=='Zprávy - Domácí':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Ostrava - Ostrava - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Hokej - NHL':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Pardubice - Pardubice - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Liberec - Liberec - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Zprávy - Zahraničí':
        df.iloc[i,5]='Svět'
    elif df.iloc[i,5]=='Sport - Volejbal':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Ekonomika - Domácí':
        df.iloc[i,5]='Ekonomika'
    elif df.iloc[i,5]=='Plzeň - Plzeň - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Hradec - Hradec - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Ústí - Ústí - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Hokej - Evropské ligy':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Sport - Florbal':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Hokej - Reprezentace':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Fotbal - První liga':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Kultura - Film/TV':
        df.iloc[i,5]='Kultura'
    elif df.iloc[i,5]=='Sport - Házená':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Ekonomika - Zahraniční':
        df.iloc[i,5]='Ekonomika'
    elif df.iloc[i,5]=='Sport - Ostatní sporty':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Hokej - NHL':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Kultura - Hudba':
        df.iloc[i,5]='Kultura'
    elif df.iloc[i,5]=='Sport - Basket':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Zlín - Zlín - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Hokej - Extraliga':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Jihlava - Jihlava - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Fotbal - Poháry':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Karlovy Vary - Vary - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Cestování - Kolem světa':
        df.iloc[i,5]='Cestování'
    elif df.iloc[i,5]=='Sport - Motorsport':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Budějovice - Budějovice - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Olomouc - Olomouc - zprávy':
        df.iloc[i,5]='Domov'
    elif df.iloc[i,5]=='Sport - Lyžování':
        df.iloc[i,5]='Sport'
    elif df.iloc[i,5]=='Auto - Zpravodajství':
        df.iloc[i,5]='Auto'

#df.insert(0,'',np.linspace(0,581,582))
df.to_csv('article_archive_all_9_12_10am_cat.csv',index=False, header=df.columns, mode='a')

# Domov
# Svět
# Sport
# Ekonomika
# Kultura
# Zdraví
# Cestování
# Věda
# Auto
# Životní styl	