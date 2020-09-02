#-*-coding:utf-8-*-

import json

dic = {'a': 1, 'b': 2, 'c': 3}
js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
# print(js)

listABC = ["a", "b", "c", "d"]
# for abc in range(len(listABC)):
#     print(abc)

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


url = 'https://instagram.fhkg4-2.fna.fbcdn.net/v/t51.2885-15/e35/34146083_1986155678364485_1625234166180216832_n.jpg?_nc_ht=instagram.fhkg4-2.fna.fbcdn.net\\u0026_nc_cat=105\\u0026_nc_ohc=jqXO0OZ2vDMAX-D6OAs\\u0026oh=4e46c3b517bb84c28175ac87086cc257\\u0026oe=5F78475F'
url.replace('\\u0026','&')
# print(url.replace('\\u0026','&'))
# print(len('window._sharedData = '))
print(len("window.__additionalDataLoaded('/p/BjtAXjWHAQr/',"))