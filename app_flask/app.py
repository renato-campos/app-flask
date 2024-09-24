from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/user/<name>')
def greet_user(name):
    return f'Hello, {name}!'



if __name__ == '__main__':
    app.run(debug=True)