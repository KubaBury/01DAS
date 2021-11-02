from flask import Flask, render_template, url_for
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
    zpravy = []
    with open('C:/Users/vacla/OneDrive/Dokumenty/GitHub/01DASteam/data/article_archive.csv', encoding="utf8") as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            zpravy.append(row)
    return zpravy

def vyber_zpravy():

    zpravy = csv2dict()
    articles_all = pd.DataFrame(zpravy)
    
    #c=np.array([0,1,2,443,314,307,306,7,10])
    #c = np.arange(0,10)
    #c = np.arange(300,310)
    #c = np.arange(0,10)
    
    #articles=articles_all.iloc[c,[1,3]]
    
    articles2 = []
    k = 0
    velikost = 0
    
    while velikost <= 14:
        c = np.arange(0,15 + k)    
        articles=articles_all.iloc[c,[1,3]]    
        vla=vectorized_lemmatized_articles(articles,0,c.shape[0])
        ded=deduplicate(vla.run())
        b=ded.run()
        if len(b) != 0:
            bb = [x+300 for x in b]
            articles2 = articles.drop(bb)
        else: 
            articles2=articles
        
        velikost = articles2.shape[0]
        k = k + 1
    
    zpravy_vybrane = articles2.to_dict('records')
    return zpravy_vybrane

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(200), nullable= False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['GET'])

def index():
    zpravy = vyber_zpravy()
    
    return render_template('index.html',
        zpravy  = zpravy,
    )

if __name__ =="__main__":
    app.run(debug=True)

