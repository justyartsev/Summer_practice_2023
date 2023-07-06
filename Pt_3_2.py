fib_number = lambda number: number if number <= 1 else fib_number(number - 1) + fib_number(number - 2)
fib_row = lambda y: [fib_number(i) for i in range(0, y)]
print(fib_row(7))
fibonacci = lambda n: [] if n == 0 else [0] if n == 1 else [0, 1] \
        + [fibonacci(n - 1)[i - 1] + fibonacci(n - 1)[i - 2] for i in range(2, n)]
