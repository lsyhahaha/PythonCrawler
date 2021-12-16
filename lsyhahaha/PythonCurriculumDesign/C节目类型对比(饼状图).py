'''一、节目类型对比【饼状图】'''

import pandas as pd
import matplotlib.pyplot as plt

'''pandas的重要数据结构DataFrame(一个带有行索引和列索引的二维表)'''
df = pd.read_csv('all_Data(已处理).csv')
df = df.drop(df.columns[[0]], axis = 1) #用索引【0，1】删除列
'''
首先，找到春晚节目类型有哪些
然后，按照一定方式分类，比较这些类型各自出现的次数
最后，绘制柱状图
'''
alist = ['歌曲','相声','小品','舞蹈','魔术','其他']

blist = [0,0,0,0,0,0]
leixing = dict(zip(alist,blist))#初始化
for i in df['类型']:
    '''只统计类型名含有关键字的行'''
    if '歌曲' in i:
        leixing['歌曲'] += 1
    elif '相声' in i:
        leixing['相声'] += 1
    elif '小品' in i:
        leixing['小品'] += 1
    elif '舞' in i:
        leixing['舞蹈'] += 1
    elif '魔术' in i:
        leixing['魔术'] += 1
    else:
        leixing['其他'] +=1
#leixing 为键为类型，值为出现次数的字典

df1 = df[df.类型.isin(['歌曲'])]
df2 = df[df.类型.isin(['小品'])]
df3 = df[df.类型.isin(['相声'])]
df4 = df[df.类型.isin(['舞蹈'])]
df5 = df[df.类型.isin(['魔术'])]
df6 = df[df.类型.isin(['其他'])]
#歌曲 371 小品172 相声108 舞蹈143 魔术13 其他309
#设置绘图的主题风格
plt.style.use('ggplot')
# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['figure.figsize']=[12,12]
# 构造数据
x = [371,172,108,143,13,309]

# 提示标签
labels = ['歌曲','小品','相声','舞蹈','魔术','其他']

# 用于突出显示歌曲数目
explode = [0.1,0,0,0,0,0]


# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0,4)
plt.ylim(0,4)

# 绘图数据
plt.pie(x, # 绘图数据
        explode=explode, # 突出显示歌曲数目
        autopct='%1.1f%%', # 设置百分比的格式，这里保留一位小数
        pctdistance=0.6, # 设置百分比标签与圆心的距离
        labeldistance=1.2, # 设置教育水平标签与圆心的距离
        startangle = 180, # 设置饼图的初始角度
        radius = 1.5, # 设置饼图的半径
        counterclock = False,
        wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},# 饼图内外边界的属性值
        textprops = {'fontsize':16, 'color':'k'}, # 设置文本标签的属性值
        center = (2,2), # 设置饼图的原点
        frame = 1, # 是否显示饼图的图框，这里设置显示
        labels=labels, # 添加教育水平标签
        )

# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())

# 添加图标题
plt.title('历年歌曲、小品、相声,舞蹈类节目数量分布饼状图')
plt.show()