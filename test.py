import urllib
import re

regex = '<td class="([^"]+)>(.+?)</td>'  
pattern = re.compile(regex)

urls = "https://origin.bankrate.com/"

htmlfile = urllib.urlopen(urls)
htmltext = htmlfile.read(htmlfile)
select   = re.findall(htmltext,pattern)

print select

