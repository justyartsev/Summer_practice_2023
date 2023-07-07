amount = int(input("Введите число: "))
not_simple = [x for x in range(2, amount+1) if any(x % i == 0 for i in range(2, int(x ** 0.5) + 1))]
print(not_simple)
