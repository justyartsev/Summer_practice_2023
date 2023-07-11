string = input("Введите строку: ")
words = string.split()
palindroms = []
for i in words:
    rev = i[::-1]
    if i == rev:
        palindroms.append(i)
print(palindroms)
