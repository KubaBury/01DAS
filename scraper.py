import feedparser
import csv
import pandas as pd

link1 = 'https://servis.idnes.cz/rss.aspx'
link2 = 'https://servis.lidovky.cz/rss.aspx'
link3 = 'https://denikn.cz/cesko/feed/?ref=inc'
link4 = 'https://www.info.cz/rss'
link5 = 'https://ct24.ceskatelevize.cz/rss/hlavni-zpravy?_ga=2.150554806.1469533093.1638876239-15973535.1607868784'
link6 = 'https://www.ceskatelevize.cz/sport/rss/vsechny-zpravy/'
link7 = 'https://www.irozhlas.cz/rss/irozhlas/section/zivotni-styl'

def feedparse(link):
    d = feedparser.parse(link)
    return d

def feed2dict(nazev,kategorie,header1,link3):
    data = {}
    link = link7
    d = feedparse(link)
    for entry in d.entries:
        data.setdefault('title', [])
        #data.setdefault('photo', [])
        data.setdefault('summary', [])
        data.setdefault('published', [])
        data.setdefault('link', [])
        data.setdefault('category', [])
        data.setdefault('source', [])
        data['title'].append(entry.title)
        #data['photo'].append(entry.media_content[0]['url'])
        #data['photo'].append(entry.enclosure[0]['url'])
        data['summary'].append(entry.summary)
        data['published'].append(entry.published)
        data['link'].append(entry.link)
        #data['category'].append(entry.category)
        data['category'].append(kategorie)
        if link == link1:
            data['source'].append('idnes.cz')
        elif link == link3:
            data['source'].append('denikn.cz')
        elif link == link5:
            data['source'].append('ČT24')
        elif link == link6:
            data['source'].append('ČT Sport')
        elif link == link7:
            data['source'].append('irozhlas.cz')
        else:
            data['source'].append('lidovky.cz')

    df = pd.DataFrame(data)
    df.to_csv(nazev,index=False, header=header1, mode='a')

# def read_csv2dict(filename):
#     with open(filename, encoding='utf-8') as f:
#         file_data=csv.reader(f)
#         headers=next(file_data)
#         return [dict(zip(headers,i)) for i in file_data]

#columns=['title','photo','summary','published','link','category','source']
columns=['title','summary','published','link','category','source']
feed2dict('data/article_archive_n14_12.csv','Životní styl',columns,link3)

#zpravy = read_csv2dict('data/article_archivenč.csv')
# #print(zpravy[0]['summary'])

