from flask import Flask, render_template
app = Flask(__name__)

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

@app.route("/") #route to main page
@app.route("/home") #route to home page
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") #route to about page
def about():
    return render_template('about.html', title='About')


if __name__=='__main__':
    app.run(debug=True)