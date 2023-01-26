geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for delete in geese:
        if delete in birds:
            birds.remove(delete)
    return birds