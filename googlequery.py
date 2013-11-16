import urllib
import mechanize
from bs4 import BeautifulSoup
import re


def googlesearch(links):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('user-agent','chrome')]

    term = links.replace(" ", "+")

    query = "http://www.google.com/search?num=100&q="+term

    htmltext = br.open(query).read()

    #print htmltext


    soup = BeautifulSoup(htmltext)
    search = soup.findAll('div',attrs={'id':'search'})
    soup1 = BeautifulSoup(str(search[0]))
    listitems =  soup1.findAll('li')

    #print listitems[0]

    regex = "q(?!.*q).*?&amp"
    pattern = re.compile(regex)

    result_list = []

    for li in listitems:
        souplinks = BeautifulSoup(str(li)).findAll('a')
        firstlink = souplinks[0]
        soupurl = re.findall(pattern, str(firstlink))
        if len(soupurl) >0:
            result_list.append(soupurl[0].replace('q=',"").replace("&amp",""))
    return result_list

print googlesearch("stock market")
