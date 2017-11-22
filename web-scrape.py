import urllib.request
from bs4 import BeautifulSoup

# Utility Functions 
def print_file(printStr):
    with open("article.txt", "w") as text_file:
        print(printStr, file=text_file)

# End Utility Functions

urlstring = 'https://www.wired.com/story/self-care-digital-detox/'

# Get Page Source Data
response = urllib.request.urlopen(urlstring)
page_source = response.read()

# Parse HTML, isolate article, convert to string
page_source_soup = BeautifulSoup(page_source, 'html.parser')
article_text = page_source_soup.article
article_text = article_text.get_text()

# Print File for data analysis
print_file(article_text)