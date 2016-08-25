# urllib提供了一系列用于操作URL的功能

# GET
# urllib的request模块可以非常方便地抓取URL内容，也就是发生一个GET请求到指定的页面，然后返回HTTP的响应:
# 例如，对豆瓣的一个URL https://api.douban.com/v2/book/2129650进行抓取，并返回响应：
# from urllib import request
# with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
#         data = f.read()
#         print('Status:', f.status,f.reason)
#         for k,v in f.getheaders():
#             print('%s:%s' %(k,v))
#         print('Data:',data.decode('utf-8'))

# 可以看到HTTP响应的头和JSON数据：
#
# Status: 200 OK
# Server: nginx
# Date: Tue, 26 May 2015 10:02:27 GMT
# Content-Type: application/json; charset=utf-8
# Content-Length: 2049
# Connection: close
# Expires: Sun, 1 Jan 2006 01:00:00 GMT
# Pragma: no-cache
# Cache-Control: must-revalidate, no-cache, private
# X-DAE-Node: pidl1
# Data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["廖雪峰编著"],"pubdate":"2007-6","tags":[{"count":20,"name":"spring","title":"spring"},{"count":11,"name":"Java","title":"Java"},{"count":6,"name":"javaee","title":"javaee"},{"count":4,"name":"j2ee","title":"j2ee"},{"count":3,"name":"POJO","title":"POJO"},{"count":3,"name":"计算机","title":"计算机"},{"count":3,"name":"藏书","title":"藏书"},{"count":3,"name":"编程","title":"编程"}],"origin_title":"","image":"https://img3.doubanio.com\/mpic\/s2648230.jpg","binding":"","translator":[],"catalog":"","pages":"509","images":{"small":"https://img3.doubanio.com\/spic\/s2648230.jpg","large":"https://img3.doubanio.com\/lpic\/s2648230.jpg","medium":"https://img3.doubanio.com\/mpic\/s2648230.jpg"},"alt":"https:\/\/book.douban.com\/subject\/2129650\/","id":"2129650","publisher":"电子工业","isbn10":"7121042622","isbn13":"9787121042621","title":"Spring 2.0核心技术与最佳实践","url":"https:\/\/api.douban.com\/v2\/book\/2129650","alt_title":"","author_intro":"","summary":"本书注重实践而又深入理论，由浅入深且详细介绍了Spring 2.0框架的几乎全部的内容，并重点突出2.0版本的新特性。本书将为读者展示如何应用Spring 2.0框架创建灵活高效的JavaEE应用，并提供了一个真正可直接部署的完整的Web应用程序——Live在线书店(http:\/\/www.livebookstore.net)。\n在介绍Spring框架的同时，本书还介绍了与Spring相关的大量第三方框架，涉及领域全面，实用性强。本书另一大特色是实用性强，易于上手，以实际项目为出发点，介绍项目开发中应遵循的最佳开发模式。\n本书还介绍了大量实践性极强的例子，并给出了完整的配置步骤，几乎覆盖了Spring 2.0版本的新特性。\n本书适合有一定Java基础的读者，对JavaEE开发人员特别有帮助。本书既可以作为Spring 2.0的学习指南，也可以作为实际项目开发的参考手册。","price":"59.80元"}

# 如果我们要想模拟浏览器发生GET请求，就需要使用Request()对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
# 例如模拟iPhone6去请求豆瓣首页。
# from urllib import request
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status , f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s' %(k,v))
#     print('data',f.read().decode('utf-8'))

# 这样豆瓣会返回适合iPhone的移动版网页

# Post
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入
# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：

# from urllib import request , parse
#
# print('Login to weibo.cn..')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# 小结

# urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能。需要把请求伪装成浏览器。伪装的方法就是先监控浏览器发出
# 的请求，在根据浏览器的请求头来伪装，user-Agent头就是用来标识浏览器的。

