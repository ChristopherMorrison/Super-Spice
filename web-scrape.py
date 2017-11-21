import urllib.request
from bs4 import BeautifulSoup

# Utility Functions 

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def print_file(printStr):
    with open("article.txt", "w") as text_file:
        print(printStr, file=text_file)


# End Utility Functions

urlstring = 'https://www.wired.com/story/self-care-digital-detox/'
printVal = 'Empty Val'

response = urllib.request.urlopen(urlstring)
page_source = response.read()

page_source_soup = BeautifulSoup(page_source, 'html.parser')
article_text = page_source_soup.article

article_text = article_text.get_text()



print_file(article_text)