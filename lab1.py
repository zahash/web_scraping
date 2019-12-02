import requests
from bs4 import BeautifulSoup
import urllib

if __name__ == '__main__':
    url = r'https://pypi.org/project/beautifulsoup4/'
    response = urllib.request.urlopen(url)
    html_page = response.read()
    soup = BeautifulSoup(html_page)
    print(soup.prettify())