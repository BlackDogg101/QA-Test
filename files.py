# var = input("Enter a variable: ")
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

# a - запись новых данных в файл и помещение новых данных в файл
# w - запись новых данных, но с удалением старых данных

# fw = open('doc/file.txt', 'w')
# fw.write("privet!!!")
# fw.close()

fr = open('doc/file.txt', 'r')
text = fr.read()
fr.close()
print(text)

def read_file(file_path):
    """Reads the content of a file and returns it."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content
print(read_file('doc/file.txt'))