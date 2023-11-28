def order(sentence: str) -> str:
    n = list.copy(sentence.split())
    for s in sentence.split():
        for i in s:
            if i.isdigit():
                n[int(i) - 1] = s
    return ' '.join(n)


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))

# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
