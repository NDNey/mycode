#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template


data = [{
    "entry":"ksdalkjf",
    "definition":"jksnd"
}

]

app = Flask(__name__)
 
@app.route("/") 
def main():
    
    try:
        print(data)
        return render_template("index.html") 
    except Exception as err:
        f"Uh-oh! {err}"

@app.route("/newEntry",methods = ["GET","POST"])
def post():
    try:
        if request.method == "POST":
            entry = request.form.get("entry") 
            definition = request.form.get("definition")
            data.append({"entry":entry,"definition":definition})
            return redirect(url_for("main"))

        else: # if a user sent a post without nm then assign value defaultuser
          return render_template("form.html" ) 
    except Exception as err:
        f"Uh-oh! {err}"


    
   
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
