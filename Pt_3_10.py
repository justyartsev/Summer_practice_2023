line = input("Введите строку: ")
dictionary = {a: line.count(a) for a in line if a != ' '}
print(dictionary)
