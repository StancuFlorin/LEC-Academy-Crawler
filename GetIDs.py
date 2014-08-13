import urllib2, cookielib
from BeautifulSoup import BeautifulSoup

#url = "http://www.lec-academy.ro/curs-php-online/"
#url = "http://www.lec-academy.ro/curs-javascript-jquery-online/"
url = "http://www.lec-academy.ro/curs-java-online/"

cookies = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
page = opener.open(url)
html = page.read()

soup = BeautifulSoup(html)
for li in soup.findAll('li'):
	if li is not None:
		if li.a is not None:
			link = li.a.get('href')
			if link.find('lectie-online') != -1 :
				print link