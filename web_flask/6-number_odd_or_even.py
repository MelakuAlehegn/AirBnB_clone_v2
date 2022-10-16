#!/usr/bin/python3
''' a script that starts a Flask web application'''


from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def nisnum(n):
    '''displays n is num if n is number'''
    return '%d is a number' % n


@app.route('/number_template', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''display a HTML page only if n is an integer:'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''display a HTML page only if n is an integer:'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
