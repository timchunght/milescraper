import requests


def right_url_content(url):
	parts = url.split("/")
	page_id = parts[len(parts)-1]
	api_url = "http://history-lab.org/api/documents/" + page_id
	return requests.get(api_url).json()["body"]





