from flask import Flask, render_template
from utilities import util

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/')
def loadHomePage():
    return render_template('index.html', strong_password=util.generatePassword())


if __name__ == '__main__':
    app.run()

