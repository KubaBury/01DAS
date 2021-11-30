import feedparser
import csv

d = feedparser.parse('https://servis.lidovky.cz/rss.aspx?r=ln_lidovky')

data = {}
for entry in d.entries:
    data.setdefault('title', [])
    data.setdefault('photo', [])
    data.setdefault('summary', [])
    data.setdefault('published', [])
    data.setdefault('link', [])
    data.setdefault('category', [])
    data.setdefault('credit', [])
    data['title'].append(entry.title)
    data['photo'].append(entry.media_content[0]['url'])
    data['summary'].append(entry.summary)
    data['published'].append(entry.published)
    data['link'].append(entry.link)
    data['category'].append(entry.category)
    data['credit'].append(entry.credit)
print(data)

data_file = open("data/article_archive_ours.csv", "w")

writer = csv.writer(data_file)
for key, value in data.items():
    writer.writerow([key, value])
data_file.close()
