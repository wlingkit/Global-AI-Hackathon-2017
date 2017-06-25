from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

def getQuestionLinksFromTag(tag):
    getMAxPageNumUrl = "http://snippets.com/tags/" + tag + ".htm"
    soup = BeautifulSoup(urllib2.urlopen(getMAxPageNumUrl).read(), "lxml")
    pagesList = soup.find_all("div", {"class", "PublicPagerTags"})
    for tags in pagesList:
        subTag = tags.find_all('a')
    maxPageNum = len(subTag)

    questions = []
    for pageNum in range(1, maxPageNum+1):
        url = "http://snippets.com/tags/" + tag + "-" + str(pageNum) + ".htm"
        soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")
        blockList = soup.find_all("a", {"class": "ItemTitle"})

        for block in blockList:
            matchObj = re.match(r'.*href="(.*)".*', str(block))
            if matchObj:
                questions.append("http://snippets.com" + matchObj.group(1))