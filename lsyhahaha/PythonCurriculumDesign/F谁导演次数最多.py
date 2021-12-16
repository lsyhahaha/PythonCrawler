'''谁导演次数最多'''

with open('导演.txt','r') as fp:
    daoyan_list = fp.readlines()
daoyan = []
for name_list in daoyan_list:
    name_split = name_list.split('、')
    for name in name_split:
        daoyan.append(name)
daoyan_dict = {}
for name in daoyan:
    if name not in daoyan_dict:
        daoyan_dict[name] = 1
    else:
        daoyan_dict[name] += 1
#结论：张晓海：4 郎昆：4 金越：3 黄一鹤：3