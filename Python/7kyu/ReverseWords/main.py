def reverse_words(text):
    return " ".join([x[::-1] for x in text.split(" ")])


print(reverse_words('double  spaced  words'))
