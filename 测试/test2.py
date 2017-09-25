# coding=utf-8
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

def get_lt():
    index_url = "http://portal.hfnu.edu.cn:8080/sso/login"
    index_page = urllib.urlopen(index_url)
    html = index_page.read()
    soup = BeautifulSoup(html, "html.parser")
    ltTemp = soup.find_all("input", type='hidden', limit=1)
    lt = ltTemp[0]['value']
    return lt

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({
		'username': '1610411010',
        'password': '300713',
        'lt': "e1s1",
        'eventId': 'submit'
		})


#登录教务系统的URL
loginUrl = 'http://portal.hfnu.edu.cn:8080/sso/login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
# cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://mh.hfnu.edu.cn/web/guest/243'
# result = opener.open(gradeUrl)

print cookie