'''钉子户排名'''

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# 解决matplotlib显示中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

'''pandas的重要数据结构DataFrame(一个带有行索引和列索引的二维表)'''
df = pd.read_csv('all_Data(已处理).csv')
df = df.drop(df.columns[[0]], axis = 1) #用索引【0】删除列

NameCount = dict()
for i in df['表演者']:
    i = list(i.split('、'))
    for ii in i:
        if ii == '表演者':
            continue
        if ii in NameCount.keys():
            NameCount[ii] += 1
        else:
            NameCount[ii] = 1
#NmaeCount为键为姓名，值为出场次数的字典

'''!!!!!到这一步只是得到大致的表演者出场次数字典，有的还没有被通缉'''

name_list = ['冯巩','姜昆','黄宏','赵本山','蔡明','彭丽媛','郭达']

name_count = [0,0,0,0,0,0,0]
res_dict = dict(zip(name_list,name_count))#初始化
for i in df['表演者']:
    i = list(i.split('、'))
    for ii in i:
        for name in name_list:
            if name in ii:
                res_dict[name] += 1
                
'''!!!!!!!res_dict才是真实结果'''
'''绘制直方图'''
plt.bar([1],28, label='冯巩')
plt.bar([2],26, label='姜昆')
plt.bar([3],24, label='黄宏')
plt.bar([4],23, label='赵本山')
plt.bar([5],22, label='蔡明')
plt.bar([6],24, label='彭丽媛')
plt.bar([7],20, label='郭达')
plt.legend()
plt.xlabel('表演者姓名')
plt.ylabel('次数')
plt.title(u'钉子户排名')