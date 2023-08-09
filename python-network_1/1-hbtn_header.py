"""documentation module"""
import requests as r
import sys as s

def __main__():
    req = r.get("https://intranet.hbtn.io")
    header = req.headers
    print(header['X-Request-Id'])
if __name__ == "__main__":
    __main__