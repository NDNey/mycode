#!/usr/bin/python3

from flask import session
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify


data = [{
    "entry": "Flask",
    "definition": "Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.",
    "user": "default"
}, {
    "entry": "Python",
    "definition": "Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.",
    "user": "default"
}
]

app = Flask(__name__)
app.secret_key = "any random string"


@app.route("/")
def main():

    if(session["username"]):
        return render_template("profile.html", entries=data, user=session["username"])
    else:
        return render_template("profile.html", entries=data)


@app.route("/entries")
def entries():
    try:
        return render_template("entries.html", entries=data)
    except Exception as err:
        f"Uh-oh! {err}"


@app.route("/newEntry", methods=["GET", "POST"])
def entry():
    try:

        if request.method == "POST":
            entry = request.form.get("entry")
            definition = request.form.get("definition")
            data.append({"entry": entry, "definition": definition,
                        "user": session["username"]})
            return redirect(url_for("main"))

        else:
            if "username" in session:
                username = session["username"]
                return render_template("form.html", user=username)
            else:
                return render_template("form.html")

    except Exception as err:
        f"Uh-oh! {err}"


@app.route("/search", methods=["GET", "POST"])
def search():
    try:
        if request.method == "POST":
            search = request.form.get("search").lower()
            print(search)
            search_result = []
            for item in data:
                if search in item["entry"].lower():
                    search_result.append(item)
            print(search_result)
            return render_template("entries.html", entries=search_result)
    except Exception as err:
        f"Uh-oh! {err}"


@app.route("/user", methods=["POST"])
def login():
    if request.method == "POST":
        print(request.form.get("name"))
        session["username"] = request.form.get("name")
        return redirect(url_for("entry"))


@app.route("/getJson")
def getJson():
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
