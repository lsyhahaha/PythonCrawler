from urllib.parse import quote

import requests

class SpringFestival:
    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}

    def get_html(self, year):
        keyword = quote('年春节联欢晚会')
        self.url = 'https://baike.baidu.com/item/{}{}'.format(year, keyword)
        print(requests.get(self.url, self.header).content.decode('utf-8'))
        return requests.get(self.url, self.header).content.decode('utf-8')

if __name__ == "__main__":
    a = SpringFestival()
    print(a.get_html(year=1983))