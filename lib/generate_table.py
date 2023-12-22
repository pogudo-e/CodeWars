import os

from dict_dirs import generate_dict


class GenerateTable:
    dictor = generate_dict()

    def __init__(self, path_file: str, home_dir: str, prefix: str):
        self.table = ''
        self.home_dir = home_dir
        self.patch_file = path_file
        self.home_readme = self.open_base_readme_file()  # Читаем заготовку
        self.home_ind = self.find_index_table_row()  # Ищем пометку для вставки
        if prefix == 'Home':
            self.generate_string_for_table_home()  # Генерируем таблицу
        elif prefix == 'Kyu':
            self.generate_string_for_table_kyu()
        self.home_readme = self.replace_text()  # Вставляем
        self.write_readme_file()
        os.system('mdformat {}'.format(self.home_dir))
        os.system('git add {}'.format(self.home_dir))

    def open_base_readme_file(self) -> list:
        """
        Open base version file to edits
        :return: text in this file
        """
        file_text = []
        with open(self.patch_file, "r") as file:
            for line in file:
                file_text.append(line)
        return file_text

    def write_readme_file(self) -> None:
        """
        Write file or update
        :return: None
        """
        with open(self.home_dir, "w+") as file:
            for k in self.home_readme:
                file.writelines(k)
        print('README.md updated: {}'.format(self.home_dir))

    def find_index_table_row(self) -> int:
        """
        Find this string to replace
        :return: index start table to write
        """
        return self.home_readme.index('[//]: # (TableRowToPaste)\n')

    def generate_string_for_table_home(self):
        # | Уровни | Решено | Ссылка |
        replace_arr = []
        for k, v in self.dictor.items():
            directory = './Python/' + k
            replace_arr.append('| {} |   {}    | [{}]({}) |'.format(k, len(v), k, directory))
        self.table = '\n'.join(replace_arr)

    def generate_string_for_table_kyu(self):
        # | Имя | Уровень | Ссылка |
        replace_arr = []
        for k, v in self.dictor.items():
            for i in v:
                directory = './' + k + '/' + i
                replace_arr.append('| {} |   {}    | [{}]({}) |'.format(i, k, i, directory))
        self.table = '\n'.join(replace_arr)

    def replace_text(self) -> list:
        """
        Replace text in index
        :return: full file
        """
        self.home_readme[self.home_ind] = self.table
        return self.home_readme


GenerateTable('README_home_dir.md', '../README.md', 'Home')
GenerateTable('README_base_lists.md', '../Python/README.md', 'Kyu')
