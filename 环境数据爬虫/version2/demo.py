import requests

# URL 地址
url = "https://link.sthj.sh.gov.cn/aqi/kqzl/kqzlCountydailydataController/getCountyDailyDataListByLst.do"

# 请求头
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://link.sthj.sh.gov.cn/"
}

# Cookie 信息（可以从浏览器开发者工具中获取）
cookies = {
    "JSESSIONID": "EF5FFDC2B752019367A8958109F0C198",
    "arialoadData": "false"
}

def get_data(area, page, cur_area_all_data):
    # 表单数据
    data = {
        "sortName": "LST",                # 排序字段
        "sortOrder": "desc",              # 排序方式
        "pageSize": "10",                 # 每页显示的数量
        "pageNumber": "{}".format(page),                # 当前页码
        "beginSearchDate": "2024-01-01",  # 开始日期
        "endSearchDate": "2024-06-30",    # 结束日期
        "searchItem": "AQI",             # 查询项
        "groupid": "{}".format(area)                  # 区域代码
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    # 打印返回的 JSON 数据
    if response.status_code == 200:
        json_data = response.json()
        # print("Total records:", json_data['total'])

        # 打印每一条数据，按照指定顺序
        for item in json_data['rows']:
            cur_area_all_data.append(item)
            print([item['ROWNUM'], item['LST'], item['PM2POINT5'], item['PM10'], item['O3'], item['SO2'], item['NO2'], item['CO'], item['AQI'], item['QUALITY'], item['PARAMETER']])
    else:
        print(f"Request failed with status code {response.status_code}")


if __name__ == "__main__":
    areas = [
        '201', '202', '203', '204', '205', '1026',
        '206', '207', '208', '209', '210', '211',
        '212', '213', '214', '215', '216', '217'
    ]

    names = [
        '浦东新区', '黄浦区', '静安区', '徐汇区', '全市平均(19站点)',
        '长宁区', '普陀区', '虹口区', '杨浦区', '闵行区', '宝山区',
        '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区'
    ]

    for i in range(len(areas)):
        print("正在抓取（{}）的数据：".format(names[i]))

        # 打印表头
        print(['序号', '日期', 'PM2.5', 'PM10', 'O3', 'SO2', 'NO2', 'CO', '实时指数', '质量评价', '首要污染物'])

        cur_area_all_data = []
        for page in range(1, 19, 1):
            get_data(areas[i], page, cur_area_all_data)
        print(cur_area_all_data)
