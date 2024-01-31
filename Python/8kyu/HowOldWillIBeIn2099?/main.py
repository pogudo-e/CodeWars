import datetime


def calculate_age(year_of_birth, current_year):
    now = datetime.datetime.now()
    diff = abs(current_year - year_of_birth)
    years = 'year' if diff == 1 else 'years'
    if diff == 0:
        return 'You were born this very year!'
    return f'You are {diff} {years} old.' if now.year > year_of_birth and year_of_birth < current_year \
        else f'You will be born in {diff} {years}.'


print(calculate_age(2012, 2016), "You are 4 years old.")
print(calculate_age(2000, 2090), "You are 90 years old.")
print(calculate_age(2000, 1990), "You will be born in 10 years.")
