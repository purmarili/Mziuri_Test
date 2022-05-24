from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_main():
    return '<h1>Welcome to our flask application</h1>'


@app.route('/<username>')
def get_user(username):
    return f'<h1>Hello {username}</h1>'


@app.route('/puppy')
def get_puppy():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5005)
    