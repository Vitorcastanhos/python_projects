from flask import Flask, render_template, request, session, make_response
import pymysql

app = Flask(__name__)

app.secret_key = "secretkey"

db = pymysql.connect(
    host="localhost", user="root", password="secretkey", database="dankicode"
)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    cursor = db.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    print(users)
    return render_template("index.html", content=users)


@app.route("/about")
def about():
    return "<h2>today is a good day!</h2>"


@app.route("/news")
def news():
    return "<h2>Raining today!</h2>"
