from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import csv

<<<<<<< Updated upstream
urls = []
for x in range(1, 5):
    urls.append("http://www.rinkworks.com/jokes/jokes" + str(x) + ".shtml")

for url in urls:
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "lxml")
    souptext = soup.get_text()
    asdf = re.split('#\d', souptext)

    with open('eggs.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for idx, jokes in enumerate(asdf):
            if idx == 0 or idx == len(asdf) -1: continue
            spamwriter.writerow([jokes, "true"])
=======
for n in range(1,2):

    url = "http://www.rinkworks.com/jokes/jokes" + str(n) + ".shtml"

    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content, "lxml")

    blockList = soup.find("div", {"class" : "content"}).find_all("ul")

    data = []
    for block in blockList:
        if len(str(block).split("\n")) == 4:
            count = 0
            modLine = ""
            for line in str(block).split("\n"):
                count = count + 1
                if (count == 2):
                    modLine =  modLine + line [4:-5]
                elif (count == 3):
                    modLine = modLine + "." + line[4:-5]
            data.append([modLine])

>>>>>>> Stashed changes

