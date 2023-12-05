import requests
import os

URL_REAL = input('Enter kata link: ')

URL_TEMPLATE = 'https://www.codewars.com/api/v1/code-challenges/{}/'.format(URL_REAL.split('/')[-1])

r = requests.get(URL_TEMPLATE)
dict_j = r.json()


class Kata:
    directory = ''
    markdown = []


kata = Kata()


def create_dir():
    kyu = str(dict_j['rank']['name']).replace(' ', '')
    name = str(dict_j['name'].title()).replace(' ', '').replace(':', '').replace(',', '')
    kata.directory = kyu + '/' + name
    if not os.path.isdir(kyu):
        os.mkdir(kyu)
        print('Directory created...{}'.format(kyu))
    else:
        print('Directory kata rang exists!')
    if not os.path.isdir(kata.directory):
        os.mkdir(kata.directory)
        print('Directory created...{}'.format(name))
    else:
        print('\tThis kata name exists!')


def markdown_cornerstone():
    kata.markdown.append('# ' + dict_j['name'] + '\n\n')
    kata.markdown.append(str(dict_j['description']) + '\n\n\n')
    kata.markdown.append('[{0}]({1})'.format(str(dict_j['slug']), str(dict_j['url'])))
    print('Description is generated...')


def generate_readme_file():
    ff = kata.directory + '/README.md'
    if not os.path.exists(ff):
        with open(ff, "w+") as file:
            for k in kata.markdown:
                file.writelines(k)
        print('README_home_dir.md created')
    else:
        print('File not created!')
    return


def generate_main_file():
    ff = kata.directory + '/main.py'
    if not os.path.exists(ff):
        with open(ff, "w+") as file:
            file.writelines('print("hello world")')
        print('main.py created')
    else:
        print('File main.py not created!')
    return


if __name__ == '__main__':
    create_dir()
    markdown_cornerstone()
    generate_readme_file()
    generate_main_file()
    print(kata.directory)
    os.system('git add {}'.format(kata.directory))
