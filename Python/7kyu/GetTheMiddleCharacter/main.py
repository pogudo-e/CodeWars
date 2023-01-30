def get_middle(s):
    res = ""
    ind = len(s)//2
    if (len(s) % 2) != 0: res = s[ind]
    else: res = s[ind-1:ind+1]
    return res

ss = "midle"

print(get_middle(ss))