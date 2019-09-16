#coding=utf8
import random,string
import random
import time
import datetime
import os
'''写一个函数方法，随机生成号码，长度11，号码开头只能以130 等开头,生成多少个号码，号码以列表的形式返回。'''
# a = '130,131,132,145,146,155,156,166,167,1704,1707,1708,1709,171,175,176,185,186'
# x = 9
#
# def create_phone_list(a, x):
#     phone_heads = a.split(',')
#     phone_list = []
#     if isinstance(x, int):
#         for i in range(int(x)):
#             phone_head = random.choice(phone_heads)
#             len_body = 11 - len(phone_head)
#             body_list = random.sample(['0','1','2','3','4','5','6','7','8','9'],  len_body)
#             body_str = ''.join(body_list)
#             phone = phone_head + body_str
#             phone_list.append(phone)
#         return phone_list
#     else:
#         print("传入的参数，不是整型")



# a = '130,131,132,145,146,155,156,166,167,1704,1707,1708,1709,171,175,176,185,186'
# x = 9
# phone_heads = a.split(',')
# phone_list = []
# for i in range(x):
#     phone_head = random.choice(phone_heads)
#     len_body = 11 - len(phone_head)
#     body_list = random.sample(['0','1','2','3','4','5','6','7','8','9'],  len_body)
#     body_str = ''.join(body_list)
#     phone = phone_head + body_str
#     phone_list.append(phone)
# print(phone_list)


# a = '130,131,132,145,146,155,156,166,167,1704,1707,1708,1709,171,175,176,185,186'
# x = 100
# phone_heads = a.split(',')
# a = [(random.choice(phone_heads) + ''.join(random.sample(string.digits,  11 - len(random.choice(phone_heads))))) for i in range(x) ]
#
# print(a)




"""写一个函数，随机生成字符串，要求：字符串可以是：数字，字母，中文，特殊字符的随机组合，而且要求可以指定某个单独的字符类型出现的次数，默认是0：
如：def create_str(a, b, c, d):
create_str(1,2,2,3)
生成：中!个s1d&*
"""




# a = '130'
# for i in range(10):
#     xp = random.choice(a)
#     len_cp = 11 - len(xp)
#     cp = ''.join(random.sample(string.digits*8,len_cp))
#     phone = xp + cp
#     print(phone)


'''
count = 0
while count <3:
    name = input("请输入用户名》》》：")
    pwd = input("请输入密码》》》：")
    if name == "谢鹏" and pwd == "123456":
        print("登录成功")
        break
    else:
        print("登陆失败")
    count+=1
'''


# a = [6,-1,4,5,6,78,99,0,88]
# print(max(a))           #求最大值
# print(min(a))           #求最小值


'''1、定义函数
'''
# def xp_abs(x=1):
#     '''计算绝对值'''
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(xp_abs(-23))



"""2、遇到return就会返回结果，而不会执行后面的结果"""
# def test(x):
#     if x >= 5:
#         return '大于5'
#     if x >= 10:
#             return '大于10'
# print(test(11))



"""小结：
        1、定义函数时，需要先确定函数名和函数个体
        2、如有必要，先对参数的数据类型做校验
        3、函数内部遇到return则会返回，而不会执行后面的结果
        4、如果函数没有return语句，则默认return None
        5、函数可以同时返回多个值，但本质上是一个元组"""


"""函数的参数
一、定义参数类型：必选参数，默认参数，可变参数，关键字参数
            目的：简化代码，方便调用
1、默认参数：可以降低调用的难度，即：少传或不传参数
"""
# def enroll(name,gender):
#     print('name',name)
#     print('gender',gender)
# enroll('多测师','谢鹏')




# randomStr = ""
# for i in range(6):
#     temp = random.randrange(0, 3)
#     if temp == 0:
#         ch = chr(random.randrange(ord('A'), ord('Z') + 1))
#         randomStr += ch
#     elif temp == 1:
#         ch = chr(random.randrange(ord('a'), ord('z') + 1))
#         randomStr += ch
#     else:
#         ch = str((random.randrange(0, 10)))
#         randomStr += ch
#
# print(randomStr)



# chin = chr(random.randint(0x4e00,0x9fbf))
# eng = [[chr(1)for i in range(65,91)]]
# num = [str(i) for i in range(10)]
# ts = ('!','@','#','$','%','&','*')
#
# def test(chinT,engT,numT,tsT,Normal=False):
#     if not Normal:
#         chinTList=[chr(random.randint(0x4e00,0x9fbf))for j in range(int(chinT))]
#     else:
#         return"0:"
# if __name__ == '__main__'
#     print(test)




# a = ['你','好']
# b = ['!','@','#','$','%','&','*']
# c = ['0','1','2','3','4','5','6','7','8','9']
# d = a + b + c
#
# F = random.shuffle(d)
# print(''.join('%s' %i for i in d))

'''写一个函数，随机生成字符串，要求：字符串可以是：数字，字母，中文，特殊字符的随机组合，而且要求可以指定某个单独的字符类型出现的次数，默认是0：'''
'''
def xp_str(a,b,c,d):        #a:数字，b:字母，c:中文，d:特殊字符
    list1=[]
    for i in range(a):
        list1.append(str(random.randint(0,9)))
    for i in range(b):
        list1.append(random.choice(string.ascii_letters))
    for i in range(c):
        list1.append(chr(random.randint(0x400,0x4e03)))
    for i in range(d):
        list1.append(random.choice(string.punctuation))
    random.shuffle(list1)
    print("".join(i for i in list1))
if __name__ == '__main__':
    xp_str(1,2,3,5)
'''

#第二种答案
"""
def create_str(num_int=0, num_letters=0, num_zh=0, num_pun=0):
    ran_list = []
    for i in range(num_int):
        # ran_list.append(str(random.randint(0, 9)))
        ran_list.append(random.choice((string.digits)))
    for i in range(num_letters):
        ran_list.append(random.choice(string.ascii_letters))
    for i in range(num_zh):
        ran_list.append(chr(random.randint(0x4e00, 0x9fbf)))
    for i in range(num_pun):
        ran_list.append(random.choice(string.punctuation))
    random.shuffle(ran_list)
    return ''.join(ran_list)
print(string.punctuation)
create_str(1,2,3,4)
"""
# a = 36.66
# print(type(a))                #打印数据类型



# a = 0
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     a = a + i
# print(a)


# b =0
# c = 99
# while c > 0:
#     b = b + c
#     c = c - 2
# print(c)


# print(os.getcwd())              #显示当前文件路径

# dcs = {
#     "name": "duoceshi",
#     "age": "4",
#     "grades1": {
#         "number": 1,
#         "teachers": ["pansir", "chensir"],
#         "students": ["xiaohong", "xiaoming", "xiaobai"],
#         "content": "python2"
#     },
#     "grades2": {
#         "number": 2,
#         "teachers": ["pansir", "chensir"],
#         "students": ["tom", "jerry", "bob"],
#         "content": "python3"
#     },
#     "grades3": {
#         "number": 3,
#         "teachers": ["pansir", "chensir"],
#         "students": ["阿毛", "阿珍", "阿强"],
#         "content": "java"
#     }
# }

#递归写法

dcs = {
    "name": "duoceshi",
    "age": "4",
    "grades1": {
        "number": 1,
        "teachers": ["pansir", "chensir"],
        "students": ["xiaohong", "xiaoming", "xiaobai"],
        "content": {"theory": "auto-test", "language": "python2"}
    },
    "grades2": {
        "number": 2,
        "teachers": ["pansir", "chensir"],
        "students": ["tom", "jerry", "bob"],
        "content": {"theory": "auto-test", "language": "python3"}
    },
    "grades3": {
        "number": 3,
        "teachers": ["pansir", "chensir"],
        "students": ["阿毛", "阿珍", "阿强"],
        "content": {"theory": "auto-test", "language": "java"}
    }
}
"""
exp = []
def get2(getkey, res_dict):
    global exp
    if isinstance(res_dict, dict):
        for k, v in res_dict.items():
            if k == getkey:
                print(v, type(v))
                # exp.append(v)
                exp = exp + v
            get2(getkey, v)
get2("teachers",dcs)
print(exp)
"""

#遍历一个字典，getkey我们需要的那个key
# def get1(getkey,res_dict):
#     for k,v in res_dict.items():
#         print(k,v)


#2、增加递归逻辑，增加字典判断，深度遍历完所有字段
# def get2(getkey,res_dict):
#     if isinstance(res_dict,dict):
#         for k,v in res_dict.items():
#             print(k,v)
#             get2(getkey,v)
# get2("grades",dcs)




dcs = {
    "name": "duoceshi",
    "age": "4",
    "grades1": {
        "number": 1,
        "teachers": ["pansir", "chensir"],
        "students": [{"shenzhen": "xiaohong"}, {"guangzhou": "xiaobai"}],
        "content": {"theory": "auto-test", "language": "python2"}
    },
    "grades2": {
        "number": 2,
        "teachers": ["pansir", "chensir"],
        "students": [{"shenzhen": "tom"}, {"guangzhou": "jerry"}],
        "content": {"theory": "auto-test", "language": "python3"}
    },
    "grades3": {
        "number": 3,
        "teachers": ["pansir", "chensir"],
        "students": [{"shenzhen": "阿珍"}, {"guangzhou": "阿强"}],
        "content": {"theory": "auto-test", "language": "java"}
    }
}

# 2. 扩展递归函数
# exp = []
# def get4(getkey, res_dict):
#     global exp
#     if isinstance(res_dict, dict):
#         for k, v in res_dict.items():
#             if k == getkey:
#                 print(v)
#                 # 把找到数据增加到exp中
#                 # exp.append(v)
#                 if isinstance(v, list):
#                     exp = exp + v
#                 break
#                 # 如果每个v只要找一个，可以手动中断
#                 # break
#             get4(getkey, v)
#     if isinstance(res_dict, list):
#         for i in res_dict:
#             get4(getkey, i)
# get4("shenzhen",dcs)
# print(exp)




# a = ['hello','world','ibm','apple']
# b = [i.upper()for i in a ]
# print(b)

# def create_str(num_int=0, num_letters=0, num_zh=0, num_pun=0):
#     ran_list = []
#     for i in range(num_int):
#         # ran_list.append(str(random.randint(0, 9)))
#         ran_list.append(random.choice((string.digits)))
#     for i in range(num_letters):
#         ran_list.append(random.choice(string.ascii_letters))
#     for i in range(num_zh):
#         ran_list.append(chr(random.randint(0x4e00, 0x9fbf)))
#     for i in range(num_pun):
#         ran_list.append(random.choice(string.punctuation))
#     random.shuffle(ran_list)
#     return ''.join(ran_list)
# print(string.punctuation)
# create_str(1,2,3,4)

# n = []
# m = [(random.choice((string.digits)))*(random.choice(string.ascii_letters)) for i in range()]
# print(m)

def create_str2(num_int=0, num_letters=0, num_zh=0, num_pun=0):
    a = [random.choice(string.digits) for i in range(int(num_int))]
    b = [random.choice(string.ascii_letters) for i in range(int(num_letters))]
    c = [chr(random.randint(0x4e00, 0x9fbf)) for i in range(int(num_zh))]
    d = [random.choice(string.punctuation) for i in range(int(num_pun))]
    ran_list = a + b + c + d
    random.shuffle(ran_list)
    return ''.join(ran_list)
# if __name__ == '__main__':
#     create_str2()
# print(create_str2)





import time


def tail(f):
    # 第一个参数：偏移量
    # 第二个参数：0，代表文件开始，1，代表文件当前位置，2，代表文件末尾
    f.seek(0, 2)  # 移动到文件最后一行
    while True:
        line = f.readline()  # 读取文件中新的文本行
        if not line:
            # 没有最新行，则每0.1秒执行一次
            time.sleep(0.1)
            # print("wait wait")
            continue
        yield line


# tail -f info.log |grep python
def grep(lines, searchtext):
    # 遍历lines生成器
    for line in lines:
        # 判断是否包含关键字
        if searchtext in line:
            # 若包含则返回
            yield line


# 模拟tail -f |grep python
# 获取生成器
flog = tail(open('test.log'))
# 把生成器当作可迭代对象传入，继续yield返回，pylines得到的也是一个生成器
pylines = grep(flog, 'python')
# 再次遍历生成器，将返回结果打印
for line in pylines:
    print(line, )




























































