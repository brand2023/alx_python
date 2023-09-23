"""flask importing"""
from flask import Flask

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

@app.route("/number/<n>", strict_slashes=False)
def numbern(n):
    if type(n) is int:
        return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)