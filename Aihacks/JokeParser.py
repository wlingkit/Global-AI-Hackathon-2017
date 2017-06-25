from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

def GetJokes():
    data = []
    for n in range(1,5):

        url = "http://www.rinkworks.com/jokes/jokes" + str(n) + ".shtml"

        content = urllib2.urlopen(url).read()

        soup = BeautifulSoup(content, "lxml")

        blockList = soup.find("div", {"class" : "content"}).find_all("ul")

        for block in blockList:
            if len(str(block).split("\n")) == 4:
                matchObj = re.match(r"<ul>\n<li>(.*)</li>\n<li>(.*)</li>\n</ul>", str(block))
                if matchObj:
                    line = str(matchObj.group(1)) + "." + str(matchObj.group(2))
                data.append([line])

    return data