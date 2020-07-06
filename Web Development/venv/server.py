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


@app.route('/<string:page_name>')
def renderPage(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'Form Submitted Successfully!'
