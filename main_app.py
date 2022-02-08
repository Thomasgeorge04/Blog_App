from flask import Flask

app = Flask(__name__)

@app.route("/") #route to main page
def hello_world():
    return "<h1>Home Page</h1>"

@app.route("/about") #route to main page
def about():
    return "<h1>About Page</h1>"


if __name__=='__main__':
    app.run(debug=True)