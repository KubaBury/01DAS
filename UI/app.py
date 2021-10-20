from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zpravy.db'
db = SQLAlchemy(app)

def csv2dict(filename):
    zpravy = []
    with open(filename, encoding="utf8") as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            zpravy.append(row)
    return zpravy


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(200), nullable= False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')

def index():
    zpravy = csv2dict('data/article_archive.csv')
    return render_template('index.html',
        zpravy  = zpravy,
    )

if __name__ =="__main__":
    app.run(debug=True)