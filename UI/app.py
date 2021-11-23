from flask import Flask, render_template, url_for , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import numpy as np
import csv
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zpravy.db'
db = SQLAlchemy(app)

def csv2dict():
    file = open("D:/Education/University/DAS/01DAS/data/article_archive.csv", encoding="utf8")
    csvreader = csv.reader(file)
    header = next(csvreader)
    zpravy_csv = []
    for row in csvreader:
        zpravy_csv.append(row)
    file.close()

    pom = zpravy_csv[0]   

    zpravy = [
        {'id': pom[0], header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]}
            ]   

    for i in range(1,np.size(zpravy_csv,0)):
        pom = zpravy_csv[i]
        zpravy.append({'id': pom[0], header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]})
    
    return zpravy


def vyber_zpravy(pocet, kategorie):
    zpravy = csv2dict()
    articles_all = pd.DataFrame(zpravy)
    articles_sort = articles_all.sort_values(by=['published'], ascending=False)

    articles2 = []
    velikost = 0
    k = 0

    while velikost <= pocet-1:
        if kategorie == 'all':
            articles_kategorie = articles_sort
        else:
            articles_kategorie = articles_sort[articles_sort['category'] == kategorie]
        articles=articles_kategorie.iloc[:pocet+k,[1,3]]    
        vla=vectorized_lemmatized_articles(articles,0,articles.shape[0])
        ded=deduplicate(vla.run())
        b=ded.run()
        if len(b) != 0:
            articles2 = articles.drop(articles.index[b])
        else: 
            articles2=articles
            
        velikost = articles2.shape[0]
        k = k + 1
    
    zpravy_vybrane = articles2.to_dict('records')
    return zpravy_vybrane

def vrat_summary(titulek):
    zpravy = csv2dict()
    articles_all = pd.DataFrame(zpravy)
    zprava = articles_all[articles_all['title']==titulek]
    return zprava['summary']


@app.route('/', methods=['GET'])

def index():
    zpravy=vyber_zpravy(9,'all')
    return render_template('index.html', zpravy=zpravy
    )


@app.route('/<kategorie>', methods=['GET'])

def category(kategorie):
    zpravy = vyber_zpravy(9,kategorie=kategorie)
    return render_template('kategorie.html',
        zpravy  = zpravy,
        page = kategorie
    )

@app.route('/<title>', methods=['GET'])

def summary(title):
    summary = vrat_summary(title=title)
    
    return render_template('summary.html',
        summary  = summary
    )



if __name__ =="__main__":
    app.run(debug=True)

