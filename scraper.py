import feedparser
import csv
import pandas as pd

link1 = 'https://servis.idnes.cz/rss.aspx'
link2 = 'https://servis.lidovky.cz/rss.aspx'

def feedparse(link):
    d = feedparser.parse(link)
    return d

def feed2dict():
    data = {}
    link = link2
    d = feedparse(link)
    for entry in d.entries:
        data.setdefault('title', [])
        data.setdefault('photo', [])
        data.setdefault('summary', [])
        data.setdefault('published', [])
        data.setdefault('link', [])
        data.setdefault('category', [])
        data.setdefault('source', [])
        data['title'].append(entry.title)
        data['photo'].append(entry.media_content[0]['url'])
        data['summary'].append(entry.summary)
        data['published'].append(entry.published)
        data['link'].append(entry.link)
        data['category'].append(entry.category)
        if link == link1:
            data['source'].append('idnes.cz')
        else:
            data['source'].append('lidovky.cz')

    df = pd.DataFrame(data)
    df.to_csv('data/article_archive2.csv',index=False, header=False, mode='a')

def read_csv2dict(filename):
    with open(filename, encoding='utf-8') as f:
        file_data=csv.reader(f)
        headers=next(file_data)
        return [dict(zip(headers,i)) for i in file_data]


feed2dict()
zpravy = read_csv2dict('data/article_archive2.csv')
print(zpravy[0]['summary'])

