from bs4 import BeautifulSoup
import urllib2
import re

data = []
for n in range(1,90):

    url = "http://www.rinkworks.com/jokes/jokes" + str(n) + ".shtml"

    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content, "lxml")

    blockList = soup.find("div", {"class" : "content"}).find_all("ul")

    # for block in blockList:
    #     if len(str(block).split("\n")) == 4:
    #         count = 0
    #         modLine = ""
    #         for line in str(block).split("\n"):
    #             count = count + 1
    #             if (count == 2):
    #                 modLine =  modLine + line [4:-5]
    #             elif (count == 3):
    #                 modLine = modLine + "." + line[4:-5]
    #         data.append([modLine])

    for block in blockList:
        if len(str(block).split("\n")) == 4:
            matchObj = re.match(r"<ul>\n<li>(.*)</li>\n<li>(.*)</li>\n</ul>", str(block))
            if matchObj:
                line = str(matchObj.group(1)) + "." + str(matchObj.group(2))
            data.append([line])