# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步是解析改HTML页面。
# 看看里面的内容到底是新闻、图片还是视频

# 假设第一步已经完成了，第二步应该如何解析HTML呢？
# html本质上是Xml的子集，但是html的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
#                 <head></head>
#                 <body>
#                 <!-- test html parser -->
#                 <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
#                 </body></html>''')
# feed()方法可以多次调用，也就是不一定把整个HTML字符串都塞进去，可以一部分一部分塞进去
# 特殊字符有两种，一种是英文表示的&nbsp;一种是数字表示的&#1234；，这两种字符都可以通过Parser解析出来

#小结

#利用HTMLParser，可以把网页中的文本、图像等解析出来。

#练习

#找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

from html.parser import HTMLParser
from html.entities import name2codepoint
from AAAurllib import request

def getHtml(url):
    req = request.Request(url)
    with request.urlopen(req) as f:
        return f.read().decode('utf-8')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.Events={}
        self._tag=''
        self._counter=0

    def handle_starttag(self, tag, attrs):
        if tag=='h3'and attrs and attrs[0][0]=='class'and  attrs[0][1]=='event-title':
            self._tag='title'
            #print('<%s>' % attrs)
        if tag=='time'and attrs and attrs[0][0]=='datetime':
            self._tag = 'datetime'
            #print('<%s>' % attrs)
        if tag == 'span'and attrs and attrs[0][0]=='class'and  attrs[0][1]=='event-location':
            self._tag = 'location'
            #print('<%s>' % attrs)

    def handle_data(self, data):
        if self._tag=='title':
            self.Events[self._counter]={'title':data.strip("\n")}
        if self._tag=='datetime':
            self.Events[self._counter]['time'] = data.strip("\n")
        if self._tag=='location':
            self.Events[self._counter]['location'] = data.strip("\n")
            self._counter += 1
        self._tag=''

    def printEvents(self):
        for k in self.Events:
            print("title:%s  Time: %s  Loaction:%s" % (
                self.Events[k]['title'], self.Events[k]['time'], self.Events[k]['location']))



if __name__=='__main__':
    parser = MyHTMLParser()
    parser.feed(getHtml('https://www.python.org/events/python-events/'))
    parser.printEvents()

