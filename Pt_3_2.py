fib_number = lambda number: number if number <= 1 else fib_number(number - 1) + fib_number(number - 2)
fib_row = lambda y: [fib_number(i) for i in range(0, y)]
print(fib_row(7))
