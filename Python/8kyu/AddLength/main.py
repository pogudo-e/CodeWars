def add_length(str_):
    return [(i + ' ' + str(len(i))) for i in str_.split()]


print(add_length('apple ban'), ["apple 5", "ban 3"])
