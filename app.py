from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from William Garofalo! I am adding my first code change'

@app.route('/hello')
def hello():
    return render_template('hello')

@app.route('/favorite-courses')
def favorite_courses():

    print('You entered your favorite course as:' + request.args.get('subject'))

    return render_template('favorite-courses.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
