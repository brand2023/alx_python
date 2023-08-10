"""documentation module"""
import requests as r
import sys as s


if __name__ == "__main__":
    email = s.argv[2]
    response = r.get(s.argv[1], email)
    postr = r.post(email)
    content = postr.text
    print(content)
    print("Your email is: ",email)