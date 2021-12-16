'''谁主持次数最多'''

with open('主持.txt','r') as fp:
    zhuchi_list = fp.readlines()
zhuchi = []
for name_list in zhuchi_list:
    name_split = name_list.split('、')
    for name_str in name_split:
        if '（' in name_str:
            name = name_str.split('（')[0]
            zhuchi.append(name)
        elif '[' in name_str:
            name = name_str.split('[')[0]
            zhuchi.append(name)
        else:
            zhuchi.append(name_str)
zhuchi_dict = {}
for name in zhuchi:
    if name not in zhuchi_dict:
        zhuchi_dict[name] = 0
    else:
        zhuchi_dict[name] += 1

'遍历字典'
for items in zhuchi_dict.items():
    print(items)