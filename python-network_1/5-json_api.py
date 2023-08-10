"""documentation module"""
import requests as r
import sys as s


if __name__ == "__main__":

    try:
        q = s.argv[1]
    except IndexError:
        q = ""

    response = r.post("http://0.0.0.0:5000/search_user", {"q": q})

    try:
        jeson = response.json()
        if len(jeson) != 0:
            print ("[{}] {}".format(jeson["id"], jeson["name"]))
        else:
            print("No result")
    except jeson.decoder.JSONDecodeError:
        print("Not a valid JSON")
