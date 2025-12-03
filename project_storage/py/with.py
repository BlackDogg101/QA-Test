# file_name = "file.txt"
# data = "Hello World"

# # fw = open(file_name, 'a')
# # fw.write(data)
# # fw.close()

# with open(file_name, 'a') as files:
#     files.write(data) 

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    with open('file_1.txt', 'a') as file_1, \
         open('file_2.txt', 'a') as file_2:
        file_1.write(f'{number}\n')
        if number % 2 == 0:
                continue
        else:
                file_2.write(f'{number}\n')
with open('file_2.txt', 'r') as file_2:
    print(file_2.read())
