from flask import Flask, render_template, request, redirect, url_for, flash, session, g
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dogs')
def dogs():
    return hello_world()

if __name__ == '__main__':
    app.run()
