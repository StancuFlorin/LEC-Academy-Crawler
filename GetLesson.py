import sys
import urllib2
from BeautifulSoup import BeautifulSoup
import cookielib

link = str(sys.argv[1])

class MyHTTPErrorProcessor(urllib2.HTTPErrorProcessor):

	def http_response(self, request, response):
		code, msg, hdrs = response.code, response.msg, response.info()

		# only add this line to stop 302 redirection.
		if code == 302: return response

		if not (200 <= code < 300):
			response = self.parent.error('http', request, response, code, msg, hdrs)
		return response

	https_response = http_response

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), MyHTTPErrorProcessor)
page = opener.open(link)
html = page.read()

soup = BeautifulSoup(html)

title = "None"
if soup.find('h1') is not None:
	title = soup.find('h1').getText()

chapper = "None"
if soup.find('h2') is not None:
	chapper = soup.find('h2').getText()

vimeo = "None"
if soup.find('iframe') is not None:
	vimeo = soup.find('iframe').get('src')

print vimeo
print title
print chapper