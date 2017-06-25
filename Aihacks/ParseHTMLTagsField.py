import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
# Returns an array with complete URL Strings for Tags from Snippets.
# ['snippets.com/tags/accessories.htm', 'snippets.com/tags/accounting.htm', etc]

def GetTags():
    url = "http://snippets.com/tags/"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "lxml")
    findalls = soup.find('p')
    tags = re.findall('<a href="\/tags\/\w*.htm', str(findalls))
    reformatted_tags = []
    for tag in tags:
        tag2 = tag.replace('<a href=/tags/"', "")
        tag3 = tag2.replace('.htm', "")
        reformatted_tags.append(tag3)
    print(reformatted_tags)
    return reformatted_tags

GetTags()