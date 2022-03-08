import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html")


@app.route("/something", methods=["POST","GET"])
def something():

    AAA = request.form["AAA"]
    BBB = request.form["BBB"]

    # do something
    CCC = AAA
    DDD = BBB
    
    return render_template("something.html", CCC=CCC, DDD=DDD)


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)