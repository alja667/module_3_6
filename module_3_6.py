def calculate_structure_sum(data_structure):

    summa = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            if isinstance((key, value), str):
                summa += len(key)
                summa += len(value)
            else:
                summa += calculate_structure_sum(key)
                summa += calculate_structure_sum(value)
    elif isinstance(data_structure, list):
        for i in data_structure:
            summa += calculate_structure_sum(i)
    elif isinstance(data_structure, tuple):
        for j in data_structure:
            summa += calculate_structure_sum(j)
    elif isinstance(data_structure, set):
        for k in data_structure:
            summa += calculate_structure_sum(k)
    elif isinstance(data_structure, int):
        summa += int(data_structure)
    elif isinstance(data_structure, float):
        summa += data_structure
    elif isinstance(data_structure, list):
        summa += len(data_structure)
    elif isinstance(data_structure, str):
        summa += len(data_structure)
    return summa


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
