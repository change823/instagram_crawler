#-*-coding:utf-8-*-
alien = {'color': 'green', 'points': 5}
# print(alien)
# print(alien['color'])
# print('points is ' + str(alien['points']))
# alien['x_pos'] = 0
# alien['y_pos'] = 25
# print(alien)

alien = {'x_pos': 0, 'speed': 'fast'}
# print('Origin X_pos: ' + str(alien['x_pos']))
if alien['speed'] == 'slow':
    x_incr = 1
elif alien['speed'] == 'medium':
    x_incr = 2
else:
    x_incr = 3
alien['x_pos'] += x_incr
# print('New X_pos: ' + str(alien['x_pos']))
# print(alien)
del alien['speed']
# print(alien)

languages = {'tom': 'java', 'jerry': 'python', 'puff': 'python'}
# print("Tom's favorite language is " + languages['tom'].title() + ".")

# for name, language in languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# print(list(languages.keys()))
# print(list(languages.values()))

friends = ['tony', 'tom']
# for name in languages:
#     print(name.title())
#     if name in friends:
#         print("    "+name.title() + "'s favorite language is " + languages[name].title() + ".")

# if 'clearlove' not in languages.keys():
#     print('Clearlove, please take our poll!')

# for name in sorted(languages.keys()):
#     print(name.title())

# for language in set(languages.values()):
#     print(language.title())

student_0 = {'name': 'a', 'age': 11}
student_1 = {'name': 'b', 'age': 12}
student_2 = {'name': 'c', 'age': 13}
students = [student_0, student_1, student_2]
# for student in students:
#     print(student)

students = []
for student_seq in range(10):
    new_student = {'name': 's', 'age': 10}
    students.append(new_student)

# for student in students[:5]:
#     print(student)
# print('\n')

# for student in students[:3]:
#     if student['name'] == 's':
#         student['name'] = 't'
#         student['age'] = 11

# for student in students[:5]:
#     print(student)
# print('\n')

# for student in students[:4]:
#     if student['name'] == 's':
#         student['name'] = 't'
#         student['age'] = 11
#     elif student['name'] == 't':
#         student['name'] = 'u'
#         student['age'] = 12

# for student in students[:5]:
#     print(student)
# print('\n')

students = {
    'name': 'tom',
    'courses': ['python', 'java'],
}

# print('Your name is ' + students['name'] + ', yours courses:')
# for course in students['courses']:
#     print('\t' + course.title())

languages = {
    'tom': ['java', 'python'],
    'jerry': ['c'],
}

# for name, languages in languages.items():
#     if len(languages) > 1:
#         print("\n" + name.title() + "'favorite languages are:")
#     else:
#         print("\n" + name.title() + "'favorite language is:")

#     for language in languages:
#         print('\t' + language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'age': 12,
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'age': 18,
    }
}

# for username, user_info in users.items():
#     print('\nUsername: ' + username.title())
#     full_name = user_info['first'] + ' ' + user_info['last']
#     age = user_info['age']

#     print('\tFull name: ' + full_name.title())
#     print('\tAge is: ' + str(age))

# msg = input('Tell me something, and I will repeat it back to you: ')
# print(msg)

# temp = 'If you tell us who you are, we can personalize the messages you see.'
# temp += '\nWhat is your name? '
# msg = input(temp)
# print('Hello, ' + msg + '!')

# age = input('Enter your age: ')
# age = int(age)
# if age >= 18:
#     print('Adult')

# number = input('Enter a number: ')
# number = int(number)
# if number % 2 == 0:
#     print(str(number) + ' is even.')
# else:
#     print(str(number) + ' is odd.')

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

temp = '\nTell me something, and I will repeat it back to you: '
temp += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     msg = input(temp)

#     if msg == 'quit':
#         active = False
#     else:
#         print(msg)

# while True:
#     msg = input(temp)

#     if 'quit' == msg:
#         break
#     else:
#         print(msg)

# cur_num = 0
# while cur_num < 10:
#     cur_num += 1
#     if cur_num % 2 == 0:
#         continue
#     print(cur_num)

unconfirmed_users = ['tom', 'jerry']
confirmed_users = []

# while unconfirmed_users:
#     cur_user = unconfirmed_users.pop()
#     print('Verify user: ' + cur_user.title())
#     confirmed_users.append(cur_user)

# print('\nAll confirmed.')
# for confirm_user in confirmed_users:
#     print(confirm_user)

# pets = ['cat', 'dog', 'cat', 'pig']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

ages = {}

# flag = True
# while flag:
#     name = input('\nEnter your name: ')
#     age = input('\nEnter your age: ')
#     ages[name] = int(age)

#     repeat = input('Have others? (yes or no)')
#     if repeat == 'no':
#         flag = False

# for name, age in ages.items():
#     print(name.title() + "'age is " + str(age))

# def greet_user(user_name):
#     """显示简单的问候语"""
#     print('Hello, ' + user_name.title() + '!')

# greet_user('tom')

# def des_pet(pet_type, pet_name):
#     '''显示宠物的信息'''
#     print('\nI have a ' + pet_type + '.')
#     print('My ' + pet_type + "'s name is " + pet_name.title())

# des_pet('mouse', 'jerry')
# des_pet(pet_name='tom', pet_type='cat')

# def desc_pet(pet_name, pet_type='dog'):
#     print('\nI have a ' + pet_type + '.')
#     print('My ' + pet_type + "'s name is " + pet_name.title())

# desc_pet('hah')
# desc_pet('haha', pet_type='cat')

# def get_full_name(first, last, middle=''):
#     if middle:
#         full_name = first + ' ' + middle + ' ' + last
#     else:
#         full_name = first + ' ' + last

#     return full_name.title()

# print(get_full_name('jimi', 'hendrix'))
# print(get_full_name('john', 'hooker', 'lee'))

# def build_person(first, last, age=''):
#     person = {
#         'first': first,
#         'last': last,
#     }
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=12)
# print(musician)


def get_full_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()


while True:
    print('\nEnter your name:')
    print("(Enter 'q' to exit.)")

    f = input('First: ')
    if f == 'q':
        break
    l = input('Last: ')
    if l == 'q':
        break

    full_name = get_full_name(f, l)
    print('Hello, ' + full_name + '!')