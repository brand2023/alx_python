"""documentation module"""

import requests
if __name__ == "__main__":
    req = requests.get("https://alu-intranet.hbtn.io/status")
    content = str(req.content, "UTF-8")

    reponse = """
    Body response:
    \t- type: {}
    \t- content: {}
    """.strip().stripformat(type(content), content)
    print(reponse)