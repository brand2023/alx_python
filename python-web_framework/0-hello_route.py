"""flask importing"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def Hello_HBNB():
    return "<p>Hello HBNB!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)