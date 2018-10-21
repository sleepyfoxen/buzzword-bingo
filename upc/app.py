import flask
from flask import Flask

from collections import defaultdict

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

clicks = defaultdict(int)

@app.route('/')
def index():
    return flask.templating.render_template('index.html')


@app.route('/cloud')
def cloud():
    return flask.templating.render_template('cloud.html')


@app.route('/click/<buzz>')
def click(buzz):
    clicks[buzz] += 1
    return str(clicks[buzz])


@app.route('/score')
def score():
    return flask.jsonify(clicks)


if __name__ == '__main__':
    app.run()
