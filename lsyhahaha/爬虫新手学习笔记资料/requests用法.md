# requests模块的入门使用

## 目标

- 掌握requests发送请求的方法
- 掌握response对象的基础属性
- 掌握requests发送带headers的请求
- 掌握requests模块发送带参数请求

## 1. 为什么要重点学习requests模块，而不是urllib

- requests的底层实现就是urllib
- requests在python2 和python3中通用，方法完全一样
- requests简单易用
- Requests能够自动帮助我们解压(gzip压缩的等)网页内容

## 2.requests的作用

作用：发送网络请求，返回响应数据

中文文档 ： [http://docs.python-requests.org/zh_CN/latest/index.html](http://docs.python-requests.org/zh_CN/latest/index.html)

通过观察文档来学习：如何使用requests来发送网络请求？

## 3. requests模块发送简单的请求、获取响应

需求：通过requests向百度首页发送请求，获取百度首页的数据

```
response = requests.get(url)

```

response的常用属性：

- `response.text`
- `respones.content`
- `response.status_code`
- `response.request.headers`
- `response.headers`

思考：text是response的属性还是方法呢？

> 一般来说名词，往往都是对象的属性，对应的动词是对象的方法

### 3.1 response.text 和response.content的区别

- `response.text`
  - 类型：str
  - 解码类型： 根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码
  - 如何修改编码方式：`response.encoding=”gbk”`
- `response.content`
  - 类型：bytes
  - 解码类型： 没有指定
  - 如何修改编码方式：`response.content.deocde(“utf8”)`

获取网页源码的通用方式：

1. `response.content.decode()`
2. `response.content.decode("GBK")`
3. `response.text`

以上三种方法从前往后尝试，能够100%的解决所有网页解码的问题

所以：更推荐使用`response.content.deocde()`的方式获取响应的html页面

### 3.2 练习：把网络上的图片保存到本地

思考：

- 以什么方式打开文件
- 保存什么格式的内容

## 4. 发送带header的请求

#### 4.1 思考

对比浏览器上百度首页的网页源码和代码中的百度首页的源码，有什么不同？

代码中的百度首页的源码非常少，为什么？

#### 4.2 为什么请求需要带上header？

模拟浏览器，欺骗服务器，获取和浏览器一致的内容

#### 4.3 header的形式：字典

`headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}`

#### 4.4 用法

`requests.get(url,headers=headers)`

## 5.发送带参数的请求

#### 5.1 什么叫做请求参数：

错误的列1： [http://www.webkaka.com/tutorial/server/2015/021013/](http://www.webkaka.com/tutorial/server/2015/021013/)

正确的例2：[https://www.baidu.com/s?wd=python&c=b](https://www.baidu.com/s?wd=python&c=b)

#### 5.2 参数的形式：字典

`kw = {'wd':'长城'}`

#### 5.3用法

`requests.get(url,params=kw)`

#### 5.4 关于参数的注意点

在url地址中，很多参数是没有用的，比如百度搜索的url地址，其中参数只有一个字段有用，其他的都可以删除

对应的，在后续的爬虫中，越到很多参数的url地址，都可以尝试删除参数