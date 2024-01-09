def warn_the_sheep(queue):
    return 'Pls go away and stop eating my sheep' if queue[::-1].index(
        "wolf") == 0 else f'Oi! Sheep number {queue[::-1].index("wolf")}! You are about to be eaten by a wolf!'


print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']),
      'Oi! Sheep number 2! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']),
      'Oi! Sheep number 5! You are about to be eaten by a wolf!')
