# students = ["Alex", "Ivan", "Nastya", "Olga"]

# for f in students:
#         print(len(f))

# fruits = ["cherry", "orange", "lime", "strawberry"]
# for fruit in fruits:
#     print(f"I love {fruit}")

# numbers = list(map(int, input().split()))
# print(numbers) 

fruits = ['яблоко', 'банан', 'вишня']

iteration_count = 0

for fruit in fruits:
    if "б" in fruit:
        print(f"В данном слове есть буква 'б', {fruit}")
        iteration_count += 1

# Вывод общего количества итераций
print(f"Количество элементов которые содержат букву 'б': {iteration_count}")

    