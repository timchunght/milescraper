from fuzzywuzzy import fuzz
from right_scraper import right_url_content
from left_scraper import left_url_content

left_url = "history-lab.org/documents/frus1969-76ve08d194"
right_url = "history-lab.org/documents/1975NEWDE04555"
left_body = left_url_content(left_url).lower().replace('\n', '').replace('\r', '')
right_body = right_url_content(right_url).lower().replace('\n', '').replace('\r', '')
# print(right_body)
print(left_body)