from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None

	try:
		baObj = BeautifulSoup(html.read(), 'html.parser')
		title = baObj.body.h1
	except AttributeError as e:
		return None
	return title

def test1():
	title = getTitle("http://www.pythonscraping.com/pages/page1.html")
	if title == None:
		print("Title not found")
	else:
		print(title)

def testsSoup():
	html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
	bsObj = BeautifulSoup(html, 'html.parser')
	nameList = bsObj.findAll("span", {"class":"green"})
	for name in nameList:
		print(name.get_text())

def findImg():
	html = urlopen("http://www.pythonscraping.com/pages/page3.html")
	bsObj = BeautifulSoup(html, 'html.parser')
	images = bsObj.findAll("img",{"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
	for image in images:
		print(image['src'])

def findTag():
	## find related tags according to its attributes
	soup.findAll(lambda tag: len(tag.attrs) == 2)

if __name__ == '__main__':
	# testsSoup()
	findImg()