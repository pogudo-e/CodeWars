import os

from dict_dirs import generate_dict


def open_base_readme_file(file_name: str) -> list:
    """
    Open base version file to edits
    :param file_name: name if base readme file to edits
    :return: text in this file
    """
    file_text = []
    with open(file_name, "r") as file:
        for line in file:
            file_text.append(line)
    return file_text


def write_readme_file(file_dir: str, home_to_write_text: list) -> None:
    """
    Write file or update
    :param home_to_write_text:
    :param file_dir: directory to save file .README_home_dir.md
    :return: None
    """
    with open(file_dir, "w+") as file:
        for k in home_to_write_text:
            file.writelines(k)
    print('README.md updated: {}'.format(file_dir))


def find_index_table_row(readme_text: list) -> int:
    """
    Find this string to replace
    :param readme_text:
    :return: index start table to write
    """
    return readme_text.index('[//]: # (TableRowToPaste)\n')


def generate_string_for_table_home(dict_full: dict) -> str:
    # | Уровни | Решено | Ссылка |
    replace_arr = []
    for k, v in dict_full.items():
        directory = './Python/' + k
        replace_arr.append('| {} |   {}    | [{}]({}) |'.format(k, len(v), k, directory))
    return '\n'.join(replace_arr)


def generate_string_for_table_kyu(dict_full: dict) -> str:
    # | Имя | Уровень | Ссылка |
    replace_arr = []
    for k, v in dict_full.items():
        for i in v:
            directory = './' + k + '/' + i
            replace_arr.append('| {} |   {}    | [{}]({}) |'.format(i, k, i, directory))
    return '\n'.join(replace_arr)


def replace_text(index: int, string_after_edit: str, readme_base: list) -> list:
    """
    Replace text in index
    :param index: found index to replace
    :param string_after_edit: text for table
    :param readme_base: file per edit
    :return: full file
    """
    readme_base[index] = string_after_edit
    return readme_base


dictor = generate_dict()  # Получаем словарь файлов

home_readme = open_base_readme_file('README_home_dir.md')  # Читаем заготовку
home_ind = find_index_table_row(home_readme)  # Ищем пометку для вставки
home_string_table = generate_string_for_table_home(dictor)  # Генерируем таблицу
home_readme = replace_text(home_ind, home_string_table, home_readme)  # Вставляем
home_dir = '../README.md'
write_readme_file(home_dir, home_readme)
os.system('mdformat {}'.format(home_dir))
os.system('git add {}'.format(home_dir))

kyu_readme = open_base_readme_file('README_base_lists.md')  # Читаем заготовку
kyu_ind = find_index_table_row(kyu_readme)  # Ищем пометку для вставки
kyu_string_table = generate_string_for_table_kyu(dictor)  # Генерируем таблицу
kyu_readme = replace_text(kyu_ind, kyu_string_table, kyu_readme)  # Вставляем
kyu_dir = '../Python/README.md'
write_readme_file(kyu_dir, kyu_readme)
os.system('mdformat {}'.format(kyu_dir))
os.system('git add {}'.format(kyu_dir))
