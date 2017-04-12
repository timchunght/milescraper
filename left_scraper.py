from lxml import etree
import requests
from io import StringIO, BytesIO




document = requests.get("http://history-lab.org/api/documents/frus1977-80v26d241")
html_text = document.json()["body"]
# tree = html.fromstring(page.content)

# print tree

parser = etree.HTMLParser()
tree = etree.parse(StringIO(html_text), parser)

result = etree.tostring(tree.getroot(),
pretty_print=True, method="html")

print result