import requests
from bs4 import BeautifulSoup


headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

name_lis=[]
herf_lis=[]
rating_Lis=[]

for url in ["https://movie.douban.com/top250?start="+str(i*25) for i in range(0,1)]:
    response = requests.get(url, headers=headers)
    soup=BeautifulSoup(response.text, "lxml")

    print(soup)
    # print(type(soup))
    
    
    for i in soup.find_all(attrs={"class":"hd"}):
        name_lis.append(i.a.span.text)
        herf_lis.append(i.a["href"])
    for i in soup.find_all(attrs={"class":"rating_num"}):
        rating_Lis.append(i.text)
        
for i in range(len(name_lis)):
    print(name_lis[i])
    print(herf_lis[i])
    print(rating_Lis[i])

