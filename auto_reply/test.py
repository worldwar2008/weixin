# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

content = "习近平访问清华大学"
url = 'http://api.pullword.com/get.php?source='+\
      content+\
      '&param1=0&param2=1'


req = urllib2.Request(url)



resp = urllib2.urlopen(req)
content = resp.read()

print content

line_list = content.split("\r\n")
k = []
v = []
for line in line_list:
    if len(line)>0:
        k.append(line.split(":")[0])
        v.append(float(line.split(":")[1]))

result = dict(zip(k,v))
result_sorted = sorted(result.items(),key=lambda x:-x[1])
print result_sorted[0][0]

gg = 'http://api.pullword.com/get.php?source=%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6%E6%98%AF%E5%A5%BD%E5%AD%A6%E6%A0%A1&param1=0&param2=1'

