def bumps(road):
    return 'Car Dead' if road.count('n') > 15 else 'Woohoo!'


print(bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")
print(bumps("nnn_n__n_n___nnnnn___n__nnn__"), "Woohoo!")