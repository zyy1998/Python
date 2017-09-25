# coding: utf-8
import urllib
import  urllib2
import re

# 糗事百科
url = 'http://www.qiushibaike.com'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

headers = {'User-Agent':user_agent}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request).read()

# print response

regex = r'<div class="content">.*?<span>(.*?)</span>.*?</div>'
duanZiRex = re.compile(regex, re.S)
duanZiList  =re.findall(duanZiRex,response)

print duanZiList[1]

f = file("糗事百科.txt".decode('utf-8'),"w+")
for item in duanZiList:
    f.writelines(str(item))
