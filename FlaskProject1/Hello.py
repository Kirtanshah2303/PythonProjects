from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
   else:
       return "<h1>Enter valid Request..</h1>"


@app.route('/route1')
def route1():
    return "<h1>This is first route</h1>"


@app.route('/route2/<name>')
def route2(name):
    return render_template('hello.html',name = name)

@app.route('/route3/<int:postID>')
def route3(postID):
    return "This is third route and passed integer value is --> %d" % postID

@app.route('/admin1')
def admin():
    return "Hello Mr.Admin.! You are assigned Admin ROLE."

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello Mr. %s.! You are assigned USER ROLE" %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))






if (__name__) == '__main__':
    app.run()
