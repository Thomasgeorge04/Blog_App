from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #route to main page
@app.route("/home") #route to home page
def home():
    return render_template('home.html')

@app.route("/about") #route to about page
def about():
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True)