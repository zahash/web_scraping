import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = r'http://quotes.toscrape.com/'
    response = requests.get(url)
    html_page = response.content
    soup = BeautifulSoup(html_page, features="html.parser")
    #print(soup.prettify())
    
    for div in soup.find_all("div", attrs={"class" : "quote"}):
        quote = div.find("span", attrs={"class" : "text"}).text
        author = div.find("small", attrs={"class" : "author"}).text
        print("quote:  ", quote)
        print("author: ", author)
        print('\n')
