import pandas as pd

df = pd.read_csv("E:/PythonCurriculumDesign/all_Data(未处理).csv",error_bad_lines=False)           	#读取csv文件
df = df.drop(df.columns[[0,1]], axis = 1) #用索引【0，1】删除列
df = df.dropna()                            #删除含有NAN的行
df.to_csv("all_Data(已处理).csv", mode='a', encoding='utf-8-sig')