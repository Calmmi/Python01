# -*- coding:utf-8 -*-
# Auth:小米  Date : 2019-08-25 11:59

import socket,re

# 爬虫基础，使用socket编程爬取网站的一张照片

# 建立客户端
client = socket.socket()
# 建立连接
client.connect(("img6.ph.126.net",80))
# 创建HTTP请求报文
request = b"GET /1qpKmsTLzvDnzxa_15Wybg==/1126744331789993046.jpg HTTP/1.1\r\nHost: img6.ph.126.net\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36\r\n\r\n"
# 发送请求
client.send(request)

# 接收第一个1024字节数据
data = client.recv(1024)

#创建一个用于保存响应数据的二进制空字符串
res = b""

while data:
    res += data
    data = client.recv(1024)

# print(res)
# 用正则表达式匹配出图片的二进制码
file = re.findall(b'\r\n\r\n(.*)',res,re.S)[0]
# print(file)

# 关闭连接
client.close()
# 创建文件，将匹配到的自己数据写入文件
with open(r"a.jpg","wb")as f:
    f.write(file)