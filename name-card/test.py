from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/bye')
def bye():
    return 'Bye!'


@app.route('/<name>')
def greet(name):
    return f'Hello {name + 12}!'


app.run(debug=True)
