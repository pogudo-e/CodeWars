import itertools

def number(lines: list) -> list:
    counter = itertools.count(start=1, step=1)
    return [str(next(counter)) + ': ' + str(x) for x in lines]


print(number(['a','b','c']))


# def number(lines):
#   return ['%d: %s' % v for v in enumerate(lines, 1)]