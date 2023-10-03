from flask import Flask,render_template
app = Flask(__name__)
print(__name__)
@app.route('/')
def hello_world():
    return render_template('wordle.html') #clock.htm is rendered
@app.route('/wordle.html')
def wordle():
    return render_template('clock.html') #wordle game  on diffrent page

