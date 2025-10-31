"""
Daniel Oluwasina
Oct 27, 2025
Lab 12, introduction to Flask
"""
from flask import Flask
from flask import render_template, url_for, redirect
#app object
app = Flask(__name__)
#set routing to loading page
@app.route('/')
def index():
    name = "Daniel Oluwasina"
    fruits = ["apples", "kiwi", "orange"]
    checkfruit = 'kiwi'
    return render_template("index.html", username = name, fruits_list = fruits, checkfruit = checkfruit)
    
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/quotes')
def quotes():
    return render_template("quotes.html")

@app.route('/login')
def login():
    return redirect(url_for('index'))

#set app to run if u run the file directly

if __name__ == "__main__":
    app.run(debug=True) 