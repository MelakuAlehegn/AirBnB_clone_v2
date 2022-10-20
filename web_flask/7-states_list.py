#!/usr/bin/python3
''' a script that starts a Flask web application'''


from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext()
def Teardown():
    storage.close()


@app.route('/states_list/<>', strict_slashes=False)
def states_list():
    '''display a HTML page for statest list'''
    state = sorted(list(storage.all("States").values()), key= lambda x: x.name)
    return render_template('7-states_list.html', state=state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
