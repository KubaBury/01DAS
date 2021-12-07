from flask import Flask, render_template, url_for , redirect
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
import csv
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from deduplicate import deduplicate
from cachetools import cached, LRUCache, TTLCache
from flask_login import UserMixin, login_user, LoginManager, logout_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    liked = db.relationship(
        'PostLike',
        foreign_keys='PostLike.user_id',
        backref='user', lazy='dynamic')

    def like_post(self, post):
        if not self.has_liked_post(post):
            like = PostLike(user_id=self.id, post_id=post.id)
            db.session.add(like)

    def unlike_post(self, post):
        if self.has_liked_post(post):
            PostLike.query.filter_by(
                user_id=self.id,
                post_id=post.id).delete()

    def has_liked_post(self, post):
        return PostLike.query.filter(
            PostLike.user_id == self.id,
            PostLike.post_id == post.id).count() > 0

class PostLike(db.Model):
    __tablename__ = 'post_like'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

@app.route('/like/<int:post_id>/<action>')
@login_required
def like_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(request.referrer)

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"} )

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Password"} )

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please choose a different one."
            )

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"} )

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Password"} )

    submit = SubmitField("Login")

def csv2dict():
    file = open("../data/article_archive.csv", encoding='utf8')
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

@cached(cache=TTLCache(maxsize=1024, ttl=1))
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



@app.route('/', methods=['GET'])
@cached(cache=TTLCache(maxsize=1024, ttl=1))
def index():
        zpravy=vyber_zpravy(9,'all')
        return render_template('index.html', zpravy=zpravy)



@app.route('/<kategorie>', methods=['GET'])
@cached(cache=TTLCache(maxsize=1024, ttl=1))
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    zpravy = vyber_zpravy(9,'all')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


if __name__ =="__main__":
    app.run(debug=True)

