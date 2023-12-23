def title_case(title: str, minor_words: str = ''):
    title = title.lower().split(' ')
    count = 0
    for i in title:
        if i == title[0]:
            title[count] = i.title()
        elif i in minor_words.lower().split(' '):
            title[count] = i.lower()
        else:
            title[count] = i.title()
        count += 1
    return ' '.join(title)


print(title_case('a clash of KINGS', 'a an the of'))
