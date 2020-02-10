import requests
from bs4 import BeautifulSoup
import json
import os
import urllib.parse

'''
this program will scrape random wikipedia pages and clusters them

'''

BASE_URL = r"https://en.wikipedia.org/"

if __name__ == "__main__":	
	topic = 'wiki/Inception'
	url = urllib.parse.urljoin(BASE_URL, topic)

	response = requests.get(url)
	html_page = response.content
	soup = BeautifulSoup(html_page, features="html.parser")
	# print(soup.find_all(text=True))
	# print(soup.prettify())


	href_links = []
	for a in soup.find_all("a", href=True):
		href = a["href"]
		if href.startswith("/wiki/"):
			href_links.append(href)

	for topic in href_links[:10]:
		url = urllib.parse.urljoin(BASE_URL, topic)
		response = requests.get(url)
		html_page = response.content
		soup = BeautifulSoup(html_page, features="html.parser")
		content = ''
		for para in soup.find_all("p"):
			content += para.text.lower().strip().replace("\t", " ").replace("\n", " ")

		with open("pages.tsv", "a") as file_obj:
			file_obj.write(url + "\t" + content + "\n")
