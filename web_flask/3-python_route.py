#!/usr/bin/python3
''' a script that starts a Flask web application'''


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''index page'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''HBNB page'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    '''displays C followed by text variable'''
    return ('C %s' % text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisfun(text='is cool'):
    '''displays python followed by text variable'''
    return ('Python %s' % text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')