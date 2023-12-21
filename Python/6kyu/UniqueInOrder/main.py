def unique_in_order(sequence: str):
    res = []
    for key, value in enumerate(list(sequence)[:-1]):
        if value != sequence[key + 1]:
            res.append(sequence[key])
    if len(sequence) > 0:
        res.append(sequence[-1])
    return res


print(unique_in_order("AAAABBBCCDAABBBB"))
