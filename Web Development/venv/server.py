# Resources: https://flask.palletsprojects.com/en/1.1.x/quickstart/
# In cmd, type the below commands:
# set FLASK_APP=server.py
# set FLASK_ENV=development # for debug mode
# To run the application: use 'flask run'

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def renderHTML():
    return render_template('index.html')

@app.route('/display')
def route1():
    return 'Hello, Route!'
