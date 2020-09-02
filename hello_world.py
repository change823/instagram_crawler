#-*-coding:utf-8-*-

msg = 'Hello World1'
# print(msg)
msg = 'Hello World2'
# print(msg)

user = 'Yida'
msg1 = 'Hello, {0}'.format(user)
msg2 = f'Hello, {user}'
# print(msg1)
# print(msg2)

name = 'ada lovalace'
# print(name.title())

name = 'Ada Lovalace'
# print(name.upper())
# print(name.lower())

first_name = 'ada'
last_name = 'lovalace'
full_name = first_name + ' ' + last_name
msg = 'Hello, ' + full_name.title() + '!'
# print(msg)

# print('\tpython')
# print('Languages:\n\tPython\n\tC\n\tJava')

msg = ' python '
# print(msg.lstrip())
# print(msg.rstrip())
# print(msg.strip())

age = 23
# print('Happy ' + str(age) + 'rd birthday!')

languages = ['python', 'java', 'goland']
# print(languages)
# print(languages[1].title())
# print(languages[-1])
languages[1] = 'javascript'
# print(languages)
languages.append('shell')
# print(languages)
languages.insert(0, 'node')
# print(languages)
del languages[-1]
# print(languages)
popped_language = languages.pop(1)
# print(popped_language)
# print(languages)
languages.remove('node')
# print(languages)

letters = ['aa', 'dd', 'cc']
# letters.sort()
# print(letters)
# letters.sort(reverse = True)
# print(letters)

# print(sorted(letters, reverse=True))
# print(letters)
# letters.reverse()
# print(letters)
# print(len(letters))
# for letter in letters:
#     print(letter.title())
#     print(letter.upper())
# print("That's all.")

# print(list(range(2, 10, 2)))
# for i in range(1, 4):
#     print(i)

# squares = []
# for i in range(1, 11):
#     squares.append(i**2)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))

# values = [val * 2 for val in range(1, 6)]
# print(values)

letters = ['a', 'b', 'c', 'd', 'e']
# print(letters[0:3])
# print(letters[1:4])
# print(letters[:4])
# print(letters[1:])
# print(letters[-3:])
# for letter in letters[:3]:
#     print(letter.title())

# print(letters)
# letters_copy = letters[:]
# print(letters_copy)
# letters.append('f')
# letters_copy.append('g')
# print(letters)
# print(letters_copy)

dims = (200, 100)
# print(dims)

# cars = ['audi', 'bMw', 'toyota']
# for car in cars:
#     if car.lower() == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# num = 1
# num2 = 2
# num3 = 3
# if num == 1 and num2 == 2 and num3 == 3:
#     print('yes')

nums = []
# print(1 in nums)  
# print(4 not in nums)    
if nums:
    for num in nums:
        print(num)
else:
    print('Empty!')
