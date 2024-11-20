data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def sum_numbers_lengths(data_structure):
    result = 0

    if isinstance(data_structure, str):
        result += len(data_structure)

    if isinstance(data_structure, bool):
        result += data_structure

    elif isinstance(data_structure, (int, float)):
        result += data_structure

    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            result += sum_numbers_lengths(item)

    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            result += sum_numbers_lengths(key)
            result += sum_numbers_lengths(value)

    return result


result = sum_numbers_lengths(data_structure)
print(result)
