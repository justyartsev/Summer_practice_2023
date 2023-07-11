first = int(input("Введите начало диапазона: "))
second = int(input("Введите конец диапазона: "))
simple_numbers = []
for i in range(first, second + 1):
    delit = 0
    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            delit += 1
    if delit == 0:
        simple_numbers.append(i)
print(simple_numbers)
