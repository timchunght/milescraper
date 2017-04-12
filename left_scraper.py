from lxml import etree
import requests
from io import StringIO, BytesIO



def left_url_content(url):

	parts = url.split("/")
	page_id = parts[len(parts)-1]
	api_url = "http://history-lab.org/api/documents/" + page_id


	document = requests.get(api_url)
	html_text = document.json()["body"]
	# tree = html.fromstring(page.content)

	# print tree

	parser = etree.HTMLParser()
	tree = etree.parse(StringIO(html_text), parser)

	result = etree.tostring(tree.getroot(),
	pretty_print=True, method="html")

	print result
	return html_text

if __name__ == "main":
	left_url_content("")
