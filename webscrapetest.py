#!/usr/bin/env python
#this is a webscrapetest.py

import urllib
urls = ["http://google.com","http://nytimes.com", "http://cnn.com"]
web = "https://origin.bankrate.com/"
i = 0

while i < len(urls):
	htmlfile = urllib.urlopen(urls[i].<h1>.?</h1>)
	htmltext = htmlfile.read()
	print htmltext
	i += 1


