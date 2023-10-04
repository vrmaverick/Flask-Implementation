from flask import Flask,render_template
app = Flask(__name__)
print(__name__)
@app.route('/')#http://127.0.0.1:5000/
def hello_world():
    return render_template('wordle.html') #clock.html is rendered
@app.route('/wordle.html') # try http://127.0.0.1:5000/wordle.html
def wordle():
    return render_template('clock.html') #wordle game  on diffrent page
@app.route('/<username>/<blog>/<int:blog_id>')#http://127.0.0.1:5000/Vedant/Using_Flask/2023
def show(username=None,blog =None,blog_id = None):
    return render_template("blog.html",name = username,blog_name = blog,blog_id = blog_id)#defining variable rules they change dynamically in html

