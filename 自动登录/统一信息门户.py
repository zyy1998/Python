# coding=utf-8
import requests
from bs4 import BeautifulSoup

url = "http://portal.hfnu.edu.cn:8080/sso/login"
session = requests.session()
html = session.get(url)
soup = BeautifulSoup(html.text, "html.parser")
ltTemp = soup.find_all("input", type='hidden', limit=1)
lt = ltTemp[0]['value']
print "lt"+lt

postData = {
'username':'',
'password':'',
'lt':lt,
'eventId':'submit'
}

html_2 = session.post(url, data=postData)
print html.text



