# coding=utf-8
import requests, time
import lxml.etree as etree

url = "https://movie.douban.com/top250?start="

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}



items = []

# 定义一个函数，获取250个电影详情页的url
def getAllurls():
    ret = []
    for k in range(10):
        response = requests.get(url + str(k * 25), headers=headers)  # 解析url，返模拟浏览器发送访问请求，返回响应对象
        response.raise_for_status() # 如果返回的状态码不是200， 则抛出异常;

        html = response.text
        # 1). 将html内容转化成xpath可以解析/匹配的格式;
        selector = etree.HTML(html)

        # 记录当前页面50个电影的url
        urls = []
        urls = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/@href')

        for i in urls:
            ret.append(i)
    return ret


def slove(url):
    response = requests.get(url, headers=headers)
    html = response.text
    # 1). 将html内容转化成xpath可以解析/匹配的格式;
    selector = etree.HTML(html)
    # 电影名
    moviename = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    print(moviename)

    # 评论
    comment = ['/comments?percent_type=h&limit=20&status=P&sort=new_score', '/comments?percent_type=m&limit=20&status=P&sort=new_score', '/comments?percent_type=l&limit=20&status=P&sort=new_score']
    # 好评
    htmlgood = requests.get(url+comment[0], headers=headers).text
    goodcoms = etree.HTML(htmlgood).xpath('//*[@id="comments"]/div/div[2]/p/span/text()')
    for com in goodcoms:
        print(com)


    # 中评
    htmlmid = requests.get(url+comment[1], headers=headers).text
    midcoms = etree.HTML(htmlmid).xpath('//*[@id="comments"]/div/div[2]/p/span/text()')
    for com in midcoms:
        print(com)

    # 差评
    htmlbad = requests.get(url + comment[2], headers=headers).text
    badcoms = etree.HTML(htmlbad).xpath('//*[@id="comments"]/div/div[2]/p/span/text()')
    for com in badcoms:
        print(com)


    return moviename, goodcoms, midcoms, badcoms


if __name__ == "__main__":
    # 首先获取所有电影详情页面的url
    urls = getAllurls()

    for url in urls:
        # 对每一个url进行分析
        # time.sleep(1)
        # 获取好评，中评，差评
        moviename, goodcoms, midcoms, badcoms = slove(url)

        with open("./comments/{}.txt".format(moviename[0]), 'w', encoding='utf-8') as fp:
            for goodcom in goodcoms:
                fp.write(goodcom)

            for midcom in midcoms:
                fp.write(midcom)

            for badcom in badcoms:
                fp.write(badcom)