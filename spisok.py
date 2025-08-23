personal = ["Alex", "Ivan", "Nastya", "Olga"]
#              0       1        2         3
result = personal[0] + " " + personal[2]
# print(result + " - лучшая пара")

number = [1, 15, 23, 4]
# #         0   1   2  3
# num_1 = number[1]
# print(num_1)
# result_num = number[1] + number[3]
# # print(result_num)

# print(personal[1:])
# # personal.append("Fedor")
# print(personal)
# pn = []
# pn.append(personal)
# pn.append(number)
# print(pn)

# numbers_list = [1, 2]
# str_list = ['one', 'two']
# result = zip(numbers_list, str_list)    # Передаем в метод названия списков, которые хотим объединить 
# print(list(result))
# print(result)

# bilet = input().split()
# # result = bilet[1] + bilet[2] + bilet[3]
# print(bilet)

# numbers = int(input("Введите номер билета:"))

# print(numbers)
# sum_elements = 0
# for element in numbers:
#     sum_elements += element # Добавляем текущий элемент к сумме
# print(f"Сумма всех элементов в списке: {sum_elements}")


# number = str(input())
# digits = tuple(map(int, str(number)))
# if sum(digits[:3]) == sum(digits[-3:]):
#     print('Счастливый')
# else:
#     print('Обычный')

q, w, e, r, t, y = input(), input(), input(), input(), input(), input()
if sum([int(q), int(w), int(e)]) == sum([int(r), int(t), int(y)]):
    print("Счастливый")
else:
    print("Обычный")

