def is_pangram(s: str) -> bool:
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # res = bool(False for char in alphabet if char not in s.lower())
    # return res
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s.lower():
            return False
    return True


print(is_pangram("The  over the lazy dog!"))
