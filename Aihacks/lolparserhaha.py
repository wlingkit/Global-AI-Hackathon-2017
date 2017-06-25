from bs4 import BeautifulSoup as soup
import re
import urllib.request


with urllib.request.urlopen('http://snippets.com/tags/accessories.htm') as url:
    s = url.read()
soup = soup(s, "lxml")
rawpagelist = soup.find_all('a', class_="ItemTitle")

bc = soup.find_all('div', class_="PublicPagerTags")
for tags in bc:
    subtag = tags.find_all('a')

numpages = len(subtag)



for questionnum in range(0,len(rawpagelist)):
    rawpagelist[questionnum] = str(rawpagelist[questionnum]).split('href="')[1]
    rawpagelist[questionnum] = rawpagelist[questionnum].split('"><')[0]


for pagenum in range (2, numpages):
    with urllib.request.urlopen('http://snippets.com/tags/accessories-'+ str(pagenum) + '.htm') as url:
        padfa = url.read()
    soup = soup(padfa, "lxml")
    print(type(soup))
    rawpagelistsub = soup.find_all('a', class_="ItemTitle")
    print(type(rawpagelistsub))
    for questionnum in range(0,len(rawpagelist)):
        rawpagelistsub[questionnum] = str(rawpagelist[questionnum]).split('href="')[1]
        rawpagelistsub[questionnum] = rawpagelist[questionnum].split('"><')[0]
    bc = soup.find_all('div', class_="PublicPagerTags")
    rawpagelist = rawpagelist + rawpagelistsub

