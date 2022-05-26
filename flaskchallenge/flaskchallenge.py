#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import requests



app = Flask(__name__)
def trivia():
    url = "https://the-trivia-api.com/api/questions?categories=film_and_tv,music,science&limit=1&region=US"
    data = requests.get(url)
    result = data.json()
    answer = result[0]["correctAnswer"]
    incorrect_answer = result[0]["incorrectAnswers"]
   
    trivia = {
        "answer" : answer,
        "choices" : incorrect_answer ,
        "question" : result[0]["question"]
    }
    
    return trivia

@app.route("/") 
def main():
    
    try:
        triviadata = trivia()
        return render_template("index.html", **triviadata) 
    except Exception as err:
        f"Uh-oh! {err}"
   
@app.route("/answer", methods = ["POST"])
def answered():

    if request.method == "POST":
        return redirect(url_for("main"))
    
   
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
