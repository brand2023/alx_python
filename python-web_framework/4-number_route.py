from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def Hello_HBNB():
    return "<p>Hello HBNB!</p>"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "<p>HBNB</p>"

@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    return "C {}".format(text)

@app.route("/python/", strict_slashes=False)
@app.route("/python/text/<int:text>", strict_slashes=False)
def ptext(text="is cool"):
    return "Python {}".format(text)

@app.route("/number/<n>", strict_slashes=False)
def numbern(n):
    if type(n) is int:
        return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)