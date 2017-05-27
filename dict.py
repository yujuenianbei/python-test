#!/usr/bin/python3
m = [('name','tom'),('age','20')]
print(m)
# 将列表转换成字典
d = dict(m)
print(d)
# 返回字典中的项的数量
t = len(d)
print(t)
# 返回键上的值
print(d['age'])
# 删除键为xx的项
del d['age']
print(d)
# 将新的值进行关联到键(age)上
d['age'] = 30
print(d['age'],d)
#判断d中是否有age
print('age' in d)

