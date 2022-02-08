from flask import Flask

app = Flask(__name__)

@app.route("/") #route to main page
def hello_world():
    return "<h1>Welcome to my site</h1>"

if __name__=='__main__':
    app.run(debug=True)