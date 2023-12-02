def sum_str(a: str, b: str):
    return str((int(a) if a else 0)+(int(b) if b else 0))


print(sum_str('9', '9'))


# def sum_str(a, b):
    # return str(int(a or 0) + int(b or 0))