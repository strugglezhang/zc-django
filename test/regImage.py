# -*- coding:utf-8 -*-

import requests
url = "http://wx.qlogo.cn/mmhead/Q3auHgzwzM48GiaoUjZKdwQI4EhumIbGPTjIt5raLktmgbc9Znn3HhA/0"
r = requests.get(url)

with open("b.jpg", "wb") as code:
    code.write(r.content)


r = requests.post("http://pic36.nipic.com/20131205/7447430_075747954000_2.jpg")
print(r.content)