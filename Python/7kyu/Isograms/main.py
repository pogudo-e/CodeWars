def is_isogram(s):
    return len(s) == len(set(s.lower()))


print(is_isogram("Dermatoglyphics"), True)
print(is_isogram("isogram"), True)
print(is_isogram("aba"), False, "same chars may not be adjacent")
