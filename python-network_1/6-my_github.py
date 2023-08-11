"""documentation module"""
import requests as r
import sys as s


if __name__ == "__main__":

    response = r.get("https://api.github.com/user")
    username = s.argv[1]
    password = s.argv[2]
    jeson = response.json()
    print (jeson["id"])
