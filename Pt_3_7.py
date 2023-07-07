dictionary = dict()
symbol = input("Введите строку: ").lower()
letters = 'ауеяыиоюэ'
for i in symbol:
    if i != ' ':
        if i in letters:
            dictionary[i] = True
        else:
            dictionary[i] = False
print(dictionary)
