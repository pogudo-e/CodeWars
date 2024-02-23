def show_sequence(n: int):
    s = ""
    r = 0
    if n > 0:
        for i in range(n+1):
            if 0 < i <= n:
                s += "+"
            r += i
            s += str(i)
    if n == 0:
        return f"{n}=0"
    if n < 0:
        return f"{n}<0"
    return f'{s} = {r}'


print(show_sequence(7))
