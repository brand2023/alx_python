"""documentation module"""
import requests as r
import sys as s


if __name__ == "__main__":

    username = s.argv[1]
    password = s.argv[2]
    response = r.get("https://api.github.com/user/{}".format(username), {"password": password})
    try:
        jeson = response.json()
        try:
            print(jeson["id"])
        except:
            print("None")
    except:
        pass
