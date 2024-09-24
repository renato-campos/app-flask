from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'This is the about page.'


@app.route('/user/<name>')
def greet_user(name):
    return f'Hello, {name}!'


@app.route('/square/<int:num>')
def squared(num):
    return f'O quadrado de {num} é {num ** 2}!'


# Rota que exibe o formulário
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Pegar os dados do formulário usando request.form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Received message from {name} with email {email}: {message}"
    return '''
        <form method="POST" action="/contact">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            Message: <textarea name="message"></textarea><br>
            <input type="submit" value="Enviar">
        </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
