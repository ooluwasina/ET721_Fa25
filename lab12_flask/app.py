"""
Daniel Oluwasina
Oct 27, 2025
Lab 12, introduction to Flask
"""
from flask import Flask
from flask import render_template, url_for
#app object
app = Flask(__name__)
#set routing to loading page
@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/quotes')
def quotes():
    return '<h1>Quotes</h1>'

#set app to run if u run the file directly

if __name__ == "__main__":
    app.run(debug=True) 