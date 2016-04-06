#贴吧爬虫
#coding:gbk
import re
import urllib.request
import os
def gethtml(url):
     page = urllib.request.urlopen(url)
     urllib.request.urlopen(url).read()
     html=page.read()
     return html.decode('utf-8')
def getimg(html):
    if (os.path.exists('photosTieBa')== False):
     os.mkdir('photosTieBa')
     x=1
     reg=r'src="(.*?\.jpg)" pic_ext'
     comreg=re.compile (reg)
     imglist=comreg.findall(html)
     for downloadimg in imglist:
         right = downloadimg.rindex('/')
         name = downloadimg.replace(downloadimg[:right+1],'')
         print (name + ' save success!')
         savepath = 'photosTieBa/'+ name
         urllib.request.urlretrieve(downloadimg,savepath)
         x+=1
html=gethtml('http://tieba.baidu.com/p/3501820767?pid=62429898156&cid=0#62429898156')
getimg(html)