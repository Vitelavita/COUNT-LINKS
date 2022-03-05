import urllib
from BeautifulSoup import *

count = int(input("enter count: "))
position= int(input("enter position: "))
number = 0
number2 = 0

url = "http://python-data.dr-chuck.net/known_by_Calah.html"
print (url)
html = urllib.urlopen(url).read()

while number<count:
	number = 0
	soup = BeautifulSoup(html)
	tags = soup("a")
	for tag in tags:
		number = number + 1
		while number2 < position:
			url = tag.get("href", None)
			print (url)
			html = urllib.urlopen(url).read()
			number2 +=1