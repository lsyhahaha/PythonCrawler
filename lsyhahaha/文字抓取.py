# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:31:22 2020

@author: 98708
"""

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://blog.csdn.net/Byeweiyang/article/details/121941721?utm_medium=distribute.pc_feed.none-task-blog-his_today-1.nonecase&depth_1-utm_source=distribute.pc_feed.none-task-blog-his_today-1.nonecase"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
    response = requests.get(url,headers = headers)
    response.encoding = 'utf-8' # document.charset
    
    
    soup = BeautifulSoup(response.text,'lxml')
    print(soup)
    
    
    with open('写入文件.txt','w',encoding='UTF-8') as fp:
        for li in soup.select('p'):
            fp.write(li.text+'\n')
            print(li.text)
    print(soup.select('.article'))
    

if __name__ == "__main__":
    main()