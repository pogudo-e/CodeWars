def row_weights(array):
    comand_one, comand_two = [], []
    if len(array) > 1:
        for idx, val in enumerate(array):
            if idx % 2 == 0:
                comand_one.append(val)
            else:
                comand_two.append(val)
        return sum(comand_one), sum(comand_two)
    return array[0], 0


# your code here


print(row_weights([50, 60, 70, 80]), (120, 140))
