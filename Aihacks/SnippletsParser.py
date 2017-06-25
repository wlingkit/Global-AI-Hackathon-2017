from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

def GetQuestionLinksFromTag(tag):
    # subTag = []
    getMAxPageNumUrl = "http://snippets.com/tags/" + tag + ".htm"
    print(getMAxPageNumUrl)
    # soup = BeautifulSoup(urllib2.urlopen(getMAxPageNumUrl).read(), "lxml")
    # pagesList = soup.find_all("div", {"class", "PublicPagerTags"})
    # for tags in pagesList:
    #     subTag = tags.find_all('a')
    # maxPageNum = len(subTag)

    questions = []
    for pageNum in range(1, 2): #maxPageNum+1):
        url = "http://snippets.com/tags/" + tag + "-" + str(pageNum) + ".htm"
        soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")
        blockList = soup.find_all("a", {"class": "ItemTitle"})

        for block in blockList:
            matchObj = re.match(r'.*href="(.*)".*', str(block))
            if matchObj:
                questions.append("http://snippets.com" + matchObj.group(1))
    return questions

def GetQuestionAndAnswer(url):
    #url = "http://snippets.com/how-many-purses-do-you-own.htm"
    content3 = urllib2.urlopen(url).read()
    soup3 = BeautifulSoup(content3, "lxml")

    question = soup3.find("title").contents[0]
    answer = soup3.find("meta")["content"]
    q_and_a = question+' '+answer

    # data=[]
    # data.append(q_and_a)

    return question, answer

def GetTags():
    tagurls = "http://snippets.com/tags/"
    content1 = urllib2.urlopen(tagurls).read()
    soup1= BeautifulSoup(content1, "lxml")
    tagout=[]
    for tag in soup1.find_all('a', href=re.compile('/tags/')):
        contents = str(tag.contents[0])
        newContents = contents.replace(" ", "-")
        tagout.append(newContents)
    return tagout