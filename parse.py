from bs4 import BeautifulSoup

html_doc = ""
with open('./tmp/text.html', 'r') as f:
    html_doc = f.read()

bs = BeautifulSoup(html_doc, 'html.parser')
print(bs.find('table'))

# Construct digraph from this table