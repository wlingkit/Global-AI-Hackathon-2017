from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

tagurls = "http://snippets.com/tags/"
content1 = urllib2.urlopen(tagurls).read()
soup1= BeautifulSoup(content1, "lxml")
tagout=[]
for tag in soup1.find_all('a', href=re.compile('/tags/')):
    tagout.append(tag.contents[0])
return tagout