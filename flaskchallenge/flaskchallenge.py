#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/") 
def main():
    return render_template("index.html") 

@app.route("/correct")
def correct():
    return "your answer is correct!"

@app.route("/answer", methods = ["POST"])
def login():

    if request.method == "POST":
        if request.form.get("answer").lower() == 'brazil': 
            return redirect(url_for("correct"))
            user = request.form.get("answer") 
        else: 
            return redirect(url_for("main"))
   
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
