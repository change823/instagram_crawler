#-*-coding:utf-8-*-

import json

dic = {'a': 1, 'b': 2, 'c': 3}
js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
# print(js)

listABC = ["a", "b", "c", "d"]
for abc in range(len(listABC)):
    print(abc)

# print('hello')


# 注释1
def exchange(a, b):  # 注释2
    m = a
    a = b
    b = m
    return (a, b)


'''
注释3
'''
"""
注释4
"""
a = 1
b = 2
# print(exchange(a, b))


def printByBool(b):
    if b == True:
        return 'True'
    else:
        return 'False'


# print(printByBool(True))

total = 'one '*2 + \
    'two '  + \
    'three'
# print(total)

paragraph = """这是一个段落，
可以由多行组成"""

# print(paragraph)

# input('\n\n按下enter退出')

print()
x = 'a'
# print(x)
# print(x, end='')
