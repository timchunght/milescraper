from fuzzywuzzy import fuzz
from right_scraper import right_url_content
from left_scraper import left_url_content


def compare(left_url, right_url):
	raw_left = left_url_content(left_url)
	new_left = "1." + "".join(raw_left.split("1.")[1:])
	# print(new_left)

	raw_right = right_url_content(right_url)
	new_right = "1." + "".join(raw_right.split("1.")[1:])

	cleaned_left = new_left.lower().replace('\n', '').replace('\r', '').replace(" ", "")
	cleaned_right = new_right.lower().replace('\n', '').replace('\r', '').replace(" ", "")
	print(cleaned_left)
	print("===================================")
	print(cleaned_right)

	percent_match = fuzz.partial_ratio(cleaned_left, cleaned_right)
	return percent_match



if __name__ == "__main__":
	left_url = "history-lab.org/documents/frus1969-76ve08d194"
	right_url = "history-lab.org/documents/1975NEWDE04555"
	percent_match = compare(left_url, right_url)
	print(percent_match)
	if percent_match > 80:
		print "Match"
	elif percent_match > 50:
		print "Partial"
	else:
		print "error"
