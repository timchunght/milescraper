from lxml import html
import requests

right_col = '//*[@id="document-show-view"]/div[3]/div[2]/div[5]'
base_url = "history-lab.org/documents/1974GUATEM00333"
url = "http://" + base_url
page = requests.get(url)
tree = html.fromstring(page.content)
result = tree.xpath(right_col)
print(result)