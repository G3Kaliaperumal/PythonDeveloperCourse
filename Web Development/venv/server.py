# Resources: https://flask.palletsprojects.com/en/1.1.x/quickstart/
# In cmd, type the below commands:
# set FLASK_APP=server.py
# set FLASK_ENV=development # for debug mode
# To run the application: use 'flask run'

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def displayName(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)
