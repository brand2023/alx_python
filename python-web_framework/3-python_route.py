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

@app.route("/python/", strict_slashes=False)
@app.route("/python/text/<int:text>", strict_slashes=False)
def ptext(text="is cool"):
    varrrR = "C %s"%text 
    return varrrR.replace("_", " ")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)