import pandas

def extract_document_links_from_csv(csv_file):
  df = pandas.read_csv(csv_file)
  left = df['FRUS Link']
  right = df['Cables Link']

  return left, right


if __name__ == "__main__":
  extract_document_links_from_csv('miles.csv')
