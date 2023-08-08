"""documentation module"""

import requests
req = requests.get("https://alu-intranet.hbtn.io/status")
content = str(req.content, "UTF-8")

reponse = """
Body response:
\t- type: {}
\t- content: {}
""".format(type(content), content)
print(reponse)