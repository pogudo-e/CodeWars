import string


def words_to_marks(s):
    dict_words = {value: key for key, value in enumerate(string.ascii_lowercase)}
    return sum(dict_words.get(i)+1 for i in s)


print(words_to_marks('attitude'), 100)
