#爬取历年春晚节目单数据
import requests,time
import pandas as pd
from urllib.parse import quote
from lxml import etree

def get_content(year):
    ''' URL 只允许一部分 ASCII 字符（数字字母和部分符号），其他的字符（如汉字）是不符合 URL 标准的。'''
    keywords = quote('年中国中央电视台春节联欢晚会')
    url = 'https://bk.tw.lvfukeji.com/zh-hans/{}{}'.format(year, keywords)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ike Gecko)'
                             'Chrome/85.0.4183.121 Safari/537.36'}
    strhtml = requests.get(url, headers=headers)

    '''pandas'''
    res_elements = etree.HTML(strhtml.text)
    table = res_elements.xpath('//table[@ class="wikitable"]')
    table = etree.tostring(table[0], encoding='utf-8').decode()
    df = pd.read_html(table, encoding='utf-8', header=0)[0]
    df = pd.DataFrame(df)

    df.to_csv("all_Data(未处理).csv", mode='a', encoding='utf-8-sig')

if __name__ == "__main__":
    for year in range(1984,2020):
        get_content(year)
        time.sleep(1)
        print("{}年爬取完成！".format(year))