import urllib.request
import re
count = 0
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/comments_283399.html"

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup("span")

for tag in tags:
	stringnumber = tag.contents
	number= int(stringnumber[0-1])
	count = count+ number
print(count)
