import urllib.request
from bs4 import BeautifulSoup

# Utility Functions 
def print_file(printStr):
    with open('article.txt', 'a') as text_file:
        print(printStr, '\n', file=text_file)
    return

def clear_file():
    with open('article.txt', 'w') as text_file:
        print('', file=text_file)
    return

# End Utility Functions

# TODO: Fix /u2009 encoding problems
#       Change article count output to be on GUI

def read_page(urlstring):
    # urlstring = 'https://www.wired.com/story/self-care-digital-detox/'

    # Get Page Source Data
    response = urllib.request.urlopen(urlstring)
    page_source = response.read()

    # Parse HTML, isolate article, convert to string
    page_source_soup = BeautifulSoup(page_source, 'html.parser')
    article_text = page_source_soup.article
    article_text = article_text.get_text()

    # Print File for data analysis
    print_file(article_text)

    return

def read_section(choice, message):
    # Determine section
    if   choice == 1:
        message.set('Getting article text from Business category')
        urlstring = 'https://www.wired.com/category/business/'
    elif choice == 2:
        message.set('Getting article text from Culture category')
        urlstring = 'https://www.wired.com/category/culture/'
    elif choice == 3:
        message.set('Getting article text from Design category')
        urlstring = 'https://www.wired.com/category/design/'
    elif choice == 4:
        message.set('Getting article text from Gear category')
        urlstring = 'https://www.wired.com/category/gear/'
    elif choice == 5:
        message.set('Getting article text from Science category')
        urlstring = 'https://www.wired.com/category/science/'
    elif choice == 6:
        message.set('Getting article text from Security category')
        urlstring = 'https://www.wired.com/category/security/'
    elif choice == 7:
        message.set('Getting article text from Transportation category')
        urlstring = 'https://www.wired.com/category/transportation/'
    else:
        urlstring = 'https://www.wired.com/'

    # Get Page Source Data
    response = urllib.request.urlopen(urlstring)
    page_source = response.read()

    page_source_soup = BeautifulSoup(page_source, 'html.parser')


    # Get list of articles
    article_urls = []
    for link in page_source_soup.find_all('a'):
        url = link.get('href')
        
        if url.startswith('/story/') and url not in article_urls:
            article_urls += [url]

    count = 0
    total = len(article_urls)
    for url_snippet in article_urls:
        count += 1
        print('Article ', count, ' of ', total)
        message.set('Article ' + str(count) + ' of ' + str(total))
        url_full = 'https://www.wired.com' + url_snippet
        read_page(url_full)
    
    message.set('Section Analysis Complete')

    return
