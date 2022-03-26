from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World..!"


@app.route('/route1')
def route1():
    return "<h1>This is first route</h1>"


@app.route('/route2/<name>')
def route2(name):
    return "This is second route and passed name is --> %s" % name

@app.route('/route3/<int:postID>')
def route3(postID):
    return "This is third route and passed integer value is --> %d" % postID



if (__name__) == '__main__':
    app.run()
