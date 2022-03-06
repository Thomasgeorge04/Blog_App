#This is a blog app that allows user to register and post blogs
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2422241e90658058902011e403344b45'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

#List of posts

posts = [
    
    {
        'author': 'Thomas George',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'February 2, 2022'
    },
    
    {
        'author': 'Mark Glasse',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'February 4, 2022'
    },
    
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 3',
        'content': 'Third Post content',
        'date_posted': 'February 6, 2022'
    }
    
]

#Route for home page
@app.route("/") #route to main page
@app.route("/home") #route to home page
def home():
    return render_template('home.html', posts=posts)

#Route for about page
@app.route("/about") #route to about page
def about():
    return render_template('about.html', title='About')

#Route for registration page
@app.route("/register", methods=['GET', 'POST']) #route to about page
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

#Route for login page
@app.route("/login", methods=['GET', 'POST']) #route to about page
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

#Allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)