def same_case(a: str, b: str):
    if a.isalpha() and b.isalpha():
        if (a.islower() and b.islower()) or a.isupper() and b.isupper():
            return 1
        return 0
    return -1
