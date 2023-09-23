"""flask importing"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    varrr = "C %s"%text
    return varrr.replace("_", " ")

@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def ptext(text = "is cool"):
    varrrR = "Python %s"%text
    return varrrR.replace("_", " ")

@app.route("/number/<int:n>", strict_slashes=False)
def numbern(n):
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_ever(n):
   return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
    app.run(debug=False)