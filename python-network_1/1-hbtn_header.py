"""documentation module"""
import requests as r
import sys as s

def __main__():
    """documentation main fonction"""
    req = r.get("https://intranet.hbtn.io")
    header = req.headers['X-Request-Id']
    return header
if __name__ == "__main__":
    __main__