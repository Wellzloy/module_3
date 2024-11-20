data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def sum_numbers_lengths(*args):
    w = len(args)
    for i in args:
        print(args[0])
    print(type(args))


sum_numbers_lengths(data_structure)
print(data_structure[0], type(data_structure[0]))
print(data_structure[1], type(data_structure[1]))
print(data_structure[2])
print(data_structure[3])
print(data_structure[4])
# print(data_structure[5])
# print(data_structure[6])
# print(data_structure[7])