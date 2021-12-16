'''春晚时间日期相同部分'''
with open('时间.txt','r') as fp:
    shijian_list = fp.readlines()
shijian_dict = {}
for shijian_str in shijian_list:
    shijian_Notyear = shijian_str.split('年')[-1]
    if shijian_Notyear not in shijian_dict:
        shijian_dict[shijian_Notyear] = 1
    else:
        shijian_dict[shijian_Notyear] += 1
'''
结论：
    三年或三年以上时间相同的：没有
    两年时间相同的：1月30日、2月15日、2月18日、2月4日、2月6日、2月9日
'''
same_date = ['1月30日','2月15日','2月18日','2月4日','2月6日','2月9日']
for date in same_date:
    print('同为{}的年份:'.format(date))
    for shijian in shijian_list:
        if date in shijian:
            print(shijian,end='')