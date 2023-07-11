import itertools

my_list = ['A', 'B', 'C']
for i in itertools.permutations(my_list, len(my_list)):
    print(i)
