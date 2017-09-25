# coding=utf-8
from requests import get,post,Session
import cookielib
from bs4 import BeautifulSoup

url = "http://portal.hfnu.edu.cn:8080/sso/login"

agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

headers={
"Origin":"http: // portal.hfnu.edu.cn:8080",
"Referer":"http://portal.hfnu.edu.cn:8080/sso/login?service=http%3A%2F%2Fmh.hfnu.edu.cn%2Fweb%2Fguest",
"Upgrade - Insecure - Requests":"1",
"User - Agent":agent
}
session = Session()
# session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')

def get_lt():
    s = Session()
    index_url = "http://portal.hfnu.edu.cn:8080/sso/login"
    index_page = s.get(index_url)
    html = index_page.text
    soup = BeautifulSoup(html, "html.parser")
    ltTemp = soup.find_all("input", type='hidden', limit=1)
    lt = ltTemp[0]['value']
    return lt

if __name__ =="__main__":
    lt = get_lt()
    postData = {
        'username': '1610411010',
        'password': '300713',
        'lt': lt,
        'eventId': 'submit'
    }
    R_1 = session.get(url,headers=headers)
    print "---first get login---"
    R_2 = session.post(url,headers=headers,data=postData)
    print "---second post login"

    # print session.cookies

    # # cookie = "LFR_SESSION_STATE_363239=1505028915165; UM_distinctid=15cb6459d540-05403fe36d91bb-37624605-144000-15cb6459d55a57; COOKIE_SUPPORT=true; CNZZDATA1261278153=1905047670-1504761541-http%253A%252F%252Fmh.hfnu.edu.cn%252F%7C1505028091; JSESSIONID=1353FEC7BAE68A363131DDF9207C535B.portal254; GUEST_LANGUAGE_ID=zh_CN"
    # cookie = session.cookies['JSESSIONID']+".portal254; GUEST_LANGUAGE_ID=zh_CN; COOKIE_SUPPORT=true"
    # print cookie
    # newHeader = {
    # "Cookie":cookie,
    # "Host":"mh.hfnu.edu.cn",
    # "Referer":"http://portal.hfnu.edu.cn:8080/sso/login?service=http%3A%2F%2Fmh.hfnu.edu.cn%2Fweb%2Fguest%2F243",
    # "Upgrade - Insecure - Requests":"1",
    # "User - Agent":"agent"
    # }

    newUrl = "http://mh.hfnu.edu.cn/web/guest/470"

    #


         # session.cookies.set_cookie(cookie="LFR_SESSION_STATE_363239=1505033586222; COOKIE_SUPPORT=true; UM_distinctid=15e6ae3b1cc8be-01fdf40f89bdb9-36624308-144000-15e6ae3b1cd706; JSESSIONID=C8D068A51BF8CFD6EF1C107595059A54.portal254; GUEST_LANGUAGE_ID=zh_CN; CNZZDATA1261278153=1558685289-1505028091-http%253A%252F%252Fmh.hfnu.edu.cn%252F%7C1505033557")
    R_3 = session.get(newUrl,headers=headers,cookies=myCookie)

    print R_3.text







