from flask import Flask, render_template, request
from flask_mysqldb import MySQL

# create flask object
app = Flask(__name__)

# connect to mysql
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "flaskuser"
app.config["MYSQL_PASSWORD"] = "password123"
app.config["MYSQL_DB"] = "employee_data"

mysql = MySQL(app)


# route data to front end
@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""
    if request.method == "POST":
        form = request.form
        name = form["name"]
        age = form["age"]
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO employees(name, age) VALUES(%s, %s)", (name, age))

        mysql.connection.commit()
        cur.close()

        msg = "Data succedfully sent"

    return render_template("index.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
