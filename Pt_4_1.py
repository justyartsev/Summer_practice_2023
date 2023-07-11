import itertools

number = int(input("Введите число: "))
number = str(number)
max_number = 0
for i in itertools.permutations(number, len(number)):
    i = int(''.join(i))
    if max_number < i:
        max_number = i
print(max_number)
