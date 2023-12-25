def people_with_age_drink(age):
    if age < 14:
        ans = 'toddy'
    elif age < 18:
        ans = 'coke'
    elif age < 21:
        ans = 'beer'
    else:
        ans = 'whisky'
    return f'drink {ans}'
