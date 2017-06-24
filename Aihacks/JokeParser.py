from bs4 import BeautifulSoup
import urllib.request as urllib2

url = "http://www.pythonforbeginners.com"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print(soup.prettify())