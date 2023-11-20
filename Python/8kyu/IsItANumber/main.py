def is_digit(s):
    try:
        tmp = float(s)
        return True
    except:
        return False


print(is_digit('-234.4'))
