import itertools

my_list = [5, 14, 3, 9, 8, 2, 1]  # 19
need_summ = 19
for i in range(2, len(my_list)):
    for j in itertools.combinations(my_list, i):
        if need_summ == sum(j):
            print(j)
