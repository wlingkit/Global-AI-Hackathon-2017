from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

url = "http://snippets.com/how-many-purses-do-you-own.htm"
content3 = urllib2.urlopen(url).read()
soup3 = BeautifulSoup(content3, "lxml")

question = soup3.find("title").contents[0]
answer = soup3.find("meta")["content"]
q_and_a = question+' '+answer

data=[]
data.append[q_and_a]
return data