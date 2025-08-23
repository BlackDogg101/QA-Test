while True:
    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        break
    except ValueError:
        print('Некорректный ввод, введите цифру')

while True:
    operator = input('Введите знак: ')
    if operator in ("+", "-", "/", "*"):
        break
    else:
        print('Допустим ввод только одного из следующих знаков: + / * -')


def calc(num1, operator, num2):

    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    try:
        if operator == '/':
            return num1 / num2
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    

print(f'Результат: {calc(num1, operator, num2)}')