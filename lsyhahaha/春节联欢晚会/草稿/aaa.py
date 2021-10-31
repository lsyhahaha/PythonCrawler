import parsel

with open('1983.html', 'r', encoding='utf-8') as fp:
    data = fp.read()


selector = parsel.Selector(data)
trs = selector.xpath('/html/body/div[3]/div[2]/div/div[1]/table/tbody/tr')
# /html/body/div[3]/div[2]/div/div[1]/table/tbody/tr[26]/td[3]/div/a
print(len(trs))
for tr in trs:
    jiemu = tr.xpath('./td[3]/div/a/text()').get()
    print(type(jiemu))