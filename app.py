from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from William Garofalo! CLass 407'


if __name__ == '__main__':
    app.run()
