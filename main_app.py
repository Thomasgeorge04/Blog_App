#This is a blog app that allows user to register and post blogs

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2422241e90658058902011e403344b45'

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
@app.route("/login") #route to about page
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

#Allows main app to run the web server
if __name__=='__main__':
    app.run(debug=True)