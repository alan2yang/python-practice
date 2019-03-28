# 1
# def get_max_profit(stock_list):
#     max_profit=0
#
#     for i in range(0,len(stock_list)):
#         for j in range(i+1,len(stock_list)):
#             profit=stock_list[j]-stock_list[i]
#             max_profit=profit if profit > max_profit else max_profit
#
#     return max_profit
#
#
# print(get_max_profit([10,7,5,8,11,9]))


# 2
# a=[1,2]
# b=["a","b"]
# d={}
# for k,v in zip(a,b):
#     d[k]=v
#
# print(d)

# 3  99乘法表
# for row in range(1, 10):
#     for col in range(1,row+1):
#         print('{}x{}={}\t'.format(col, row, col*(row)), end='')
#     print()

# 4

# list_a = [
#     {"name": "p1", "score": 100},
#     {"name": "p2", "score": 10},
#     {"name": "p3", "score": 30},
#     {"name": "p4", "score": 40},
#     {"name": "p5", "score": 60},
# ]
# # print(list_a[0].items())
#
# list_a.sort(key=lambda k:k.get("score"))
#
# print(list_a)

# s = [{1: "a"}, {3: "c"}, {2: "b"}]
#
# print(sorted(s, key=lambda x: list(x.values())[0]))


# 5

# def f(a, b, c="1", d="2", *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
#     print(kwargs)
#     print("hi")
#
# f(1,2,)
#
# f(b=1, a=2)
# # f(a=1, 2, c=1)  ----X
# f(1,2,d=3, f=4)
# # f(*(1, 2), **{"c":1, "d": 2, "a": 5})  ---X
# f(*(1, 2), **{"c":3, "d": 4})
#
# f(*(1,), **{"c":1, "d": 2, "b": 5})


# 6
# list_b = [12, 232, 22, 2, 2, 3, 22, 22, 32]
#
# odd_list=[x[1] for x in  filter(lambda x:x[0]%2 != 0,enumerate(list_b))]
# print(odd_list)

# print(list(zip("ab",(1,2))))
# print(list(enumerate(list_b)))


# 7
# def lonesum(*args):
#     new_args=set(args)
#     return sum(new_args)
#
# print(lonesum(1,2,3))
# print(lonesum(1,2,3,2))
# print(lonesum(3,3,3))


# 8
# def mirrorEnds(s):
#     rev_s=s[::-1]
#     for i in range(len(s)):
#         if s[:i+1]!=rev_s[:i+1]:
#             return s[:i]
#         if s[:i+1]==rev_s[:i+1]:
#             continue
#     return s
#
# print(mirrorEnds("abXYZba"))
# print(mirrorEnds("abca"))
# print(mirrorEnds("aba"))

# 9
# 设计一个装饰器retry_test(n)  作用是装饰一个函数时，传入参数n值, 当被装饰的函数产生异常的时候,
# 就重复随机间隔0-1秒，重复执行被装饰的函数, 重复执行的次数为n。
# 提示: n   为int 类型的值
# 随机间隔时间可以用random模块

# from functools import wraps
# import time
#
#
# def retry_test(retry_time=3,delay_time=0.1,return_value=None):  # 装饰器
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*arg,**kwargs):
#             for i in range(retry_time):
#                 try:
#                     func(*arg,**kwargs)
#                     return
#                 except Exception as e:
#                     time.sleep(delay_time)
#             return return_value
#
#         return wrapper
#     return decorator
#
#
# @retry_test(5)
# def run_requests():
#     print("函数正在执行！！！")
#     raise("函数异常！！！")   # 这是自定义异常
#
#
# run_requests()


# 10
# import  re
# s='kkk 192.288.1.136 kkk 192.168.1.137 kk 192.168.1.138 kk'
# l=re.findall(r'(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)',s)
# print(l)
#
# # 11
# def multiply(x, y=None):
#     def result(m):
#         print(x * m)
#
#     if isinstance(y, int) or isinstance(y, float):
#         print(x * y)
#     else:
#         return result
#
#
# multiply(2, 3.2)
# multiply(2)(3.2)

# 11
# dic={"a":1,"b":[2]}
# new_dic=dic.copy()
#
# dic['a']=11
# dic['b'].append(3)
#
# print(dic)
# print(new_dic)


# 12
# class Single(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls,*args,**kwargs)
#         return cls.instance
#
#
# obj1=Single()
# obj2=Single()
#
# obj1.attr1='value1'
# print(obj1.attr1,obj2.attr1)
# print(obj1 is obj2)


# 13

# def fabnaci(n):
#     a,b,i=0,1,0
#     while i<n:
#         yield b
#         a,b=b,a+b
#         i+=1
#
#
# print(next(fabnaci(4)))
# print("-------------")
# for i in fabnaci(5):
#     print(i)


# 14
# import copy
#
# dic={}
# li=[]
#
# for i in range(5):
#     dic["num"]=i
#     new_dic=copy.deepcopy(dic)
#     li.append(new_dic)
#
# print(li)


# 15
# import re
#
# import numpy as np
#
# s=np.arange(1,10).reshape(3,3)
# print(s)
#
# print(s[:,1])
#
#
# pat=re.compile(r'\"(.*)\"')
# txt='Computer says "no." Phone says "yes."'
# print(pat.findall(txt))
#
# pat2=re.compile(r'\"(.*?)\"')
# print(pat2.findall(txt))
#
#
# # search只返回第一个匹配成功的字符串
# ret = re.search(r'\d+', '阅读次数为 9999, 点赞数为:100')
# print(ret.group())
#
# # 从头开始满足正则表达式要求则匹配失败
# ret = re.search(r'^\d+', '阅读次数为 9999, 点赞数为:100')
# print(ret)
# print(ret.group())


# 16

# import json
#
# new_dic=json.load(open("file.json"))
#
# json.dump({"a":1,"b":2},"file.json")
#
# dic=json.loads('{"a":1,"b":2}')
# print(dic)
# print(type(dic))
#
# json_str=json.dumps({"a":11,"b":22})
# print(json_str)
# print(type(json_str))


# 17

# def outFun(a):
#     def inFun(x):
#         return a * x
#
#     return inFun
#
#
# fucn_1=[outFun(i) for i in range(3)]
#
# print(fucn_1[0](1))
# print(fucn_1[1](1))
# print(fucn_1[2](1))
#
#
# print("*******************")
# func_2=[lambda x:a*x for a in range(3)]
# print(func_2[0](1))
# print(func_2[1](1))
# print(func_2[2](1))


# 18

# def outFun(func):
#     print("哈哈")
#     def inFun():
#         print("add 功能")
#         print("这里是内层函数打印: ", func)
#         func()
#
#     return inFun
#
#
# @outFun
# def fun():
#     print("this is fun")


# 19


# li=[(1,2),(11,15),(13,12),(5,7),(22,34)]
#
# li.sort()
# print(li)
#
# li.sort(key=lambda x:x[1])
# print(li)


# 20
file_path='./深浅拷贝01.py'
# with open(file_path,'rb') as f:
#     for content in f:
#         print(content)

# with open(file_path, 'rb') as f:
#     while True:
#         line = f.readline()
#         if line:
#             print(line)
#         else:
#             break


# def get_lines(file_path):
#     with open(file_path, 'rb') as f:
#         while True:
#             data = f.readline(6000)
#             if data:
#                 yield data
#             else:
#                 break
#
#
# for line in get_lines(file_path):
#     print(line)


# 21

# l1 = ['b', 'c', 'd', 'c', 'a', 'a']
# l2 = sorted(set(l1), key=l1.index)
# print(l2)


# 22

def fib(n):
    current = 0
    num1, num2 = 0, 1

    while current < n:
        num1, num2 = num2, num1 + num2
        current += 1

        yield num1

    return 'done'

a=fib(5)

for i in a:
    print(i)