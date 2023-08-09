"""documentation module"""

from requests import get
"""response documentation"""
req = get("https://alu-intranet.hbtn.io/status")
content = str(req.content, "UTF-8")

reponse = """
Body response:
\t- type: {}
\t- content: {}
""".strip().stripformat(type(content), content)
print(reponse)