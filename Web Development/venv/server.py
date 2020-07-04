# Resources: https://flask.palletsprojects.com/en/1.1.x/quickstart/
# In cmd, type the below commands:
# set FLASK_APP=server.py
# set FLASK_ENV=development # for debug mode
# To run the application: use 'flask run'

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def default():
    return render_template('index.html')


@app.route('/index.html')
def renderIndexPage():
    return render_template('index.html')


@app.route('/work.html')
def renderWorkPage():
    return render_template('work.html')


@app.route('/works.html')
def renderWorksPage():
    return render_template('works.html')


@app.route('/about.html')
def renderAboutPage():
    return render_template('about.html')


@app.route('/contact.html')
def renderContactPage():
    return render_template('contact.html')


@app.route('/components.html')
def renderComponentPage():
    return render_template('components.html')
