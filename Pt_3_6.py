dictionary = dict()
for i in range(1, 10 + 1):
    b = ''
    n = i
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    dictionary[i] = b
print(dictionary)
