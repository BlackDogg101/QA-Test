# # # spisok
# # family_1 = ["Alex", "Olga", "Semen", "Nastya", "Alex"]
# # print(family_1)

# # # mnogestva
# # family_2 = {"Alex", "Olga", "Semen", "Nastya", "alex"}
# # print(family_2)

# # # slovar
# family_3 = {
#     "father": "Alex",
#     "mother": "Olga",
#     "son": "Semen",
#     "daughter": "Nastya",
#     "brother": "Alex"
# }
# # print(family_3["father"])  # выводит "Alex"
# for k, v in family_3.items():
#     print(f"{k} - {v}")  # выводит ключи и значения словаря

# person = {
#     "name": "Alex",
#     "age": 30,
#     "city": "SPB",
# }

# values = person.values()
# print(values)

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'b': 3, 'c': 4}
dict = dict_1 - dict_2
print(dict)