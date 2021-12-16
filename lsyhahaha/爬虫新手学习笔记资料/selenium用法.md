## 无头浏览器

##### 学习目标

1. 了解 selenium的作用
2. 了解 driver的安装过程

> 我们如果想在python爬虫操作动态的数据,就必须学习selenium自动化测试工具, 而使用selenium的前提是需要无头浏览器(无界面浏览器)

### 1 什么是selenium

Selenium是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器），可以接收指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏

### 2 PhantomJS的介绍

PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript

- 下载地址：[http://phantomjs.org/download.html](http://phantomjs.org/download.html)

### 3 Chromedriver的介绍

Chromedriver 也是一个能够被selenium驱动的浏览器，但是和PhantomJS的区别在于它是有界面的

- 下载地址：[https://npm.taobao.org/mirrors/chromedriver](https://npm.taobao.org/mirrors/chromedriver)

### 4 driver的安装

最简单的安装方式是：解压后把bin目录下的可执行文件移动到环境变量下，比如`/usr/bin` 或者是`/usr/local/bin`下面

### 5 PhantomJS安装示例

###### 5.1 下载PhantomJS：

```
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

```

##### 5.2 解压并创建软连接：

```
tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 
sudo cp -R phantomjs-2.1.1-linux-x86_64 /usr/local/share/ 
sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/

```

### 6 chromedriver安装示例

```
----- Linux 下安装方式
chromedriver_linux64.zip : 版本 ChromeDriver v2.22 (2016-06-06)
（支持 Chrome v49-52，当前Ubuntu虚拟机下的Chrome版本为50.0）


1. unzip chromedriver_linux64.zip
2. sudo chmod +x chromedriver
3. sudo mv chromedriver /usr/local/bin/


----- MacOS X 下安装方式
chromedriver_mac64.zip : 版本 ChromeDriver v2.32 (2017-08-30)
（支持 Chrome v59-61）

1. 安装 同Linux



----- Windows 下安装方式
chromedriver_win32.zip : 版本 ChromeDriver v2.32 (2017-08-30)
（支持 Chrome v59-61）

1. 解压 chromedriver_win32.zip
2. 将 chromedriver 移动到 Python安装目录下
（其实放哪都可以，但是需要配环境变量，放Python安装目录下省事）


注意：Chromedriver和电脑上的chrome版本有对应关系，建议使用最新的Chromedriver版本并且更新chrome浏览器到最新版

```

### 小结

1. 能够安装PhtantomJs和Chromedriver浏览器
2. 能够知道selenium是自动化测试工具









## selenium的基本使用

##### 学习目标

1. 掌握 selenium发送请求，加载网页的方法
2. 掌握 selenium简单的元素定位的方法
3. 掌握 selenium的基础属性和方法
4. 掌握 selenium退出的方法

> 当我们安装完毕无界面浏览器之后, 再学习下 selenium中drvier的使用操作

### 1 加载网页：

```python
# selenium通过控制浏览器，所以对应的获取的数据都是elements中的内容

from selenium import webdriver 
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")
driver.save_screenshot("长城.png")
```

### 2 定位和操作：

```python
driver.find_element_by_id(“kw”).send_keys(“长城”)
driver.find_element_by_id("su").click()
```

### 3 查看请求信息：

```python
driver.page_source
driver.get_cookies()
driver.current_url
```

### 4 退出

```python
driver.close() #退出当前页面
driver.quit()  #退出浏览器
```