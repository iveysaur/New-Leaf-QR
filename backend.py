from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dresses')
def dresses():
    return 'dresses'

@app.route('/patterns')
def patterns():
    return 'patterns'

@app.route('/shirts')
def shirts():
    return 'shirts'

@app.route('/cutouts')
def cutouts():
    return 'cutouts'

@app.route('/hats')
def hats():
    return 'hats'

@app.route('/paths')
def paths():
    return 'paths'

if __name__ == "__main__":
    app.run()
