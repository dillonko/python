import urllib
import mechanize
from bs4 import BeautifulSoup
from urlparse import urlparse

def getpic(search):
	try:
		browser = mechanize.Browser()
		browser.set_handle_robot(False)
		browser.addheaders = [('User-agent','Mozilla')]
		
		htmltext = browser.open("http://www.google.com/?t=lm")
		img_urls = []
		soup = BeautifulSoup(htmltext)
		results = soup.findall("a")

		print results
	except:
		print "error"

getpic("occupy wall street")
