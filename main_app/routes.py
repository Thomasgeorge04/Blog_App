from flask import render_template, url_for, flash, redirect
from main_app import app
from main_app.forms import RegistrationForm, LoginForm
from main_app.models import User, Post

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
