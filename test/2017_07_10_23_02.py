#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib,urllib.request
#re模块主要包含了正则表达式
import re,requests
#定义一个getHtml()函数

def getHtml(url):
    page = urllib.request.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    # page = requests.post(url,verify=False)
    # html = page.text #read()方法用于读取URL上的数据
    html = page.read()
    html = html.decode('utf-8')  # python3
    # print(type(html))
    print(html)
    return html

def getImg(html):
    reg = ""   #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    print(imgre)
    imglist = imgre.findall(html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    print(imglist)
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0

    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl,'./%s.jpg' % x)
        x+=1
#
#
html = getHtml("https://mp.weixin.qq.com/s/EEnWbUKdV2H1MC_eNIHftw")
print (getImg(html))

'''
page = urllib.request.urlopen('https://mp.weixin.qq.com/s/EEnWbUKdV2H1MC_eNIHftw')  #urllib.urlopen()方法用于打开一个URL地址
html = page.read() #read()方
print(html)
import requests
url = 'https://mp.weixin.qq.com/s/EEnWbUKdV2H1MC_eNIHftw'
r= requests.post(url)
print(r.text)
'''