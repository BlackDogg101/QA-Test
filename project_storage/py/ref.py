# def identification(name):
#     print('Вы являетесь')

#     if name == 'Alex':
#         print('Автором')

#     else:
#         print('Студентом')

# name = input('Введите Ваше Имя: ')
# identification(name)
              

# def identification(name):
#     print('Вы являетесь')

#     if name == 'Alex':
#         result = 'Автором'

#     else:
#         result = 'Студентом'

#     return result

# name = input('Введите Ваше Имя: ')
# # print(identification(name))
# n = 'Alex '
# s = identification(name)
# print(n + s)

def identification(name):
    print('Вы являетесь')

    if name == 'Alex':
        result = 'Автором'

    else:
        result = 'Студентом'

    return result

def status(result):
    print(result)

name = input('Введите Ваше Имя: ')

status(identification(name))