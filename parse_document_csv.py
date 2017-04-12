import pandas

from compare import compare
def extract_document_links_from_csv(csv_file):
  df = pandas.read_csv(csv_file)

  links = df[['Pair ID', 'FRUS Link', 'Cables Link']]
  # print links
  return links


if __name__ == "__main__":
  links = extract_document_links_from_csv('miles.csv')
  for index, link in links.iterrows():
    left_url = link['FRUS Link']
    right_url = link['Cables Link']
    pair_id = link['Pair ID']
    if(int(pair_id) >= 2025):
      print "Pair ID: {}, Left Url: {}, Right Url: {}, Percent Match: {}".format(pair_id, left_url, right_url, compare(left_url, right_url))
