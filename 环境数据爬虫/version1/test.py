import csv
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://link.sthj.sh.gov.cn/aqi/wholeCityDaily/wholeCityDailySearch.jsp"

TIMEOUT = 1

def get_html(page, area):
    # 设置无头模式（可选）
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 不打开浏览器界面
    # 启动浏览器
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(TIMEOUT)

    # 访问目标网站
    driver.get(url)

    # 显式等待结束日期输入框加载
    wait = WebDriverWait(driver, TIMEOUT)  # 最多等待10秒

    # 输入开始日期
    start_element = driver.find_element(By.XPATH, '//*[@id="beginSearchDate"]')
    js = 'document.getElementById("beginSearchDate").removeAttribute("readonly")'
    driver.execute_script(js)
    start_element.clear()
    start_element.send_keys('2024-01-01')

    # 输入结束日期
    end_element = driver.find_element(By.XPATH, '//*[@id="endSearchDate"]')
    js = 'document.getElementById("endSearchDate").removeAttribute("readonly")'
    driver.execute_script(js)
    end_element.clear()
    end_element.send_keys('2024-06-30')

    select_element = driver.find_element(By.ID, "groupId")
    # 创建 Select 对象
    select = Select(select_element)
    # 根据 value 属性选择对应的区域
    select.select_by_value(area)  # area 为具体的区域代码，例如 '201'

    # 点击查询按钮
    driver.find_element(By.XPATH, '//*[@id="search"]/input[3]').click()

    # 等待页面加载
    time.sleep(1)

    # 点击翻页按钮（假设翻页按钮是文本为页码的链接）
    page_button_xpath = f"//a[text()='{page}']"  # 翻页按钮，点击页码进行翻页
    try:
        # 等待翻页按钮可点击
        next_button = WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, page_button_xpath))
        )
        next_button.click()

        # 等待翻页后的页面加载，确保数据更新
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="aqiList"]/tbody/tr'))
        )

        # 确保 JavaScript 动作完成，页面内容更新
        WebDriverWait(driver, TIMEOUT).until(
            EC.invisibility_of_element_located((By.XPATH, '//*[@id="loading-indicator"]'))  # 假设页面有加载提示，等待其消失
        )

        # 获取网页内容
        html_content = driver.page_source
        # print(html_content)
    except Exception as e:
        print(f"Error: {e}")

    # 关闭浏览器
    driver.quit()

    return html_content

def parse(soup):
    data = list()
    rows = soup.find('tbody').find_all('tr')

    # 遍历每一行
    for row in rows:
        cur = []
        # 在每一行中查找所有 td 标签
        columns = row.find_all('td')
        # 提取并打印每一列的数据
        for column in columns:
            cur_cell = column.text.strip()
            cur.append(cur_cell)

        data.append(cur)

    return data


def run(page, area):
    html_content = get_html(page, area)

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # 现在你可以用 BeautifulSoup 进行解析

    #解析网页数据, 返回当前页面的数据
    datas = parse(soup)

    return datas

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
        area = areas[i]
        print("正在抓取（{}）的数据：".format(names[i]))

        all_data = []
        for page in range(1, 19, 1):
            try:
                datas = run(page, area)
                if datas is None:
                    continue

                for data in datas:
                    all_data.append(data)
                    print(data)
            except Exception as e:
                print(f"Error: {e}")
                continue

        #保存文件
        file_name = "{}2024年01月01日至2024年06月30日空气质量数据.csv".format(names[i])

        # 打开文件并写入数据
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # 写入表头（可以根据需要修改）
            header = ['序号', '日期', 'PM2.5', 'PM10', 'O3', 'SO2', 'NO2', 'CO', '实时指数', '质量评价', '首要污染物']
            writer.writerow(header)
            # 写入数据

            for x in all_data:
                # print(x)
                writer.writerow(x)