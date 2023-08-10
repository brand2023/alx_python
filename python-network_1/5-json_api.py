"""documentation module"""
import requests as r
import sys as s


if __name__ == "__main__":
    q=s.argv[1]

    if len(q) == 0:
        q = ""
    response = r.post("http://0.0.0.0:5000/search_user", {"q": q})
    jeson = response.json()
    if response.status_code == 200:
        if len(jeson) != 0:
            print ("[{}] {}".format(jeson["id"], jeson["name"]))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
