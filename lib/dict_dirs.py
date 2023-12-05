import os


def kyu_parse():
    directory = '../Python/'
    files = os.listdir(directory)
    kyu = []
    for g in files:
        if '.py' not in g:
            if '.md' not in g:
                kyu.append(g)
    kyu.sort()
    return kyu


def generate_dict():
    dictor = {}
    for i in kyu_parse():
        directory = '../Python/' + i
        files = os.listdir(directory)
        dirs = []
        for g in files:
            if '.py' not in g:
                if '.md' not in g:
                    dirs.append(g)
        dirs.sort()
        dictor[i] = dirs
    return dictor
