from functools import reduce
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average = reduce(lambda summ, next: summ + next, your_list) / len(your_list)
print(average)
