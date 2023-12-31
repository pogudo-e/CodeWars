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


def operatr(dir):
    def gen(func):
        def wrapper():
            print('hobaaa')
            print(dir)
            return func()

        return wrapper

    return gen


@operatr('../Python/')
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


# def scan_dir(path, level=1, ):
#     global no_git
#     no_git = os.listdir(path)
#     if level == 1:
#         no_git.remove('.git')
#
#     s = path.split('/')
#     for i in no_git:
#         if os.path.isdir(path + '/' + i):
#             scan_dir(path + '/' + i, level + 1)
#         else:
#             s = path.split('/')[1:]
#             print(s[1])
#             # if (s[0]) not in dictor.keys():
#             #     dictor[s[0]] = os.listdir(path)
#             # else:
#             #     ar = dictor[s[0]]
#             #     ar.append(os.listdir(path))
#             #     dictor[s[0]] = os.listdir(path)
#             #     if s[0][1] not in dictor.keys():
#             #         dictor[s[0][1]] = os.listdir(path)
#                 # dictor[(path + '/' + i)[4:].replace('/', ' - ')] = os.listdir(path)
#
#
# # dictor = {}


if __name__ == '__main__':
    print(generate_dict())
    # print(kyu_parse())
    # scan_dir('../')
    # print(dictor)
    # for k, v in dictor.items():
    #     print(f'{k} - {v}')
