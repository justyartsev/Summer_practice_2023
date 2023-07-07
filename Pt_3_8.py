dictionary = dict()
ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
count = 1
for i in ABC:
    dictionary[i] = count
    count += 1
print(dictionary)
