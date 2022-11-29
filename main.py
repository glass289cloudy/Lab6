from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/students_list")
def students_list():
    f = open('base/students_list.json', encoding="utf8")
    ld = json.load(f)
    lst = ld["students"]
    return render_template('students_list.html', students=lst)


if __name__ == "__main__":
    app.run()