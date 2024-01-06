def reverse_letter(string):
    ch, res = list(map(chr, range(97, 123))), ''
    for i in range(len(string)):
        if string[i] in ch:
            res = res + string[i]
    return res[::-1]



print(reverse_letter("krishan"),"nahsirk")



# def reverse_letter(string):
    # return ''.join(filter(str.isalpha, reversed(string)))