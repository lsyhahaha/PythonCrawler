''' 导演
    主持
    时间
    列表抓取'''
import requests,json,time
from urllib.parse import quote
from bs4 import BeautifulSoup


def get_content(year):
    ''' URL 只允许一部分 ASCII 字符（数字字母和部分符号），其他的字符（如汉字）是不符合 URL 标准的。'''
    keywords = quote('年中国中央电视台春节联欢晚会')
    url = 'https://bk.tw.lvfukeji.com/zh-hans/{}{}'.format(year,keywords)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, \
            ike Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    strhtml = requests.get(url,headers=headers)
    soup = BeautifulSoup(strhtml.text, 'lxml')  # lxml解析网页文档

    '''年份'''
    data = soup.select('h1',class_="firstHeading")
    print(data[0].text)

    '''导演和主持'''
    data1 = soup.find_all('td', class_ = 'attendee')
    for i in range(2):
        if i==0:
            daoyan.append(data1[i].text)
        else:
            zhuchi.append(data1[i].text)

    '''日期'''
    data2 = soup.find_all('td')
    for i in data2:
        if '北京时间' in str(i.a):
            shijian.append(i.text.split('日')[0]+'日')


if __name__ == '__main__':
    daoyan = []
    zhuchi = []
    shijian = []
    for year in range(1984,2015):
        time.sleep(1)
        get_content(year)
    for year in range(2016,2020):
        time.sleep(1) 
        get_content(year)
    
    with open('导演.txt','w') as fp:
        for name in daoyan:
            fp.write(name+'\n')
    
    with open('主持.txt','w') as fp:
        for name in zhuchi:
            fp.write(name+'\n')
            
    # with open('时间.txt','w') as fp:
    #     for date in shijian:
    #         fp.write(date+'\n')