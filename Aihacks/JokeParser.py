from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import csv

urls = []
for x in range(1, 2):
    urls.append("http://www.rinkworks.com/jokes/jokes" + str(x) + ".shtml")

for url in urls:
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "lxml")
    souptext = soup.get_text()
    asdf = re.split('#\d', souptext)

    with open('eggs.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for idx, jokes in enumerate(asdf):
            if idx == 0 or idx == len(asdf) -1: continue
            print(jokes)
