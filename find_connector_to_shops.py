import os
from typing import Iterable
import re


def gen_files_path(path_work: str, find_o: str, list_dir_magaz: list) -> Iterable[str]:
    """
    функция-генератор рекурсивно обходит рабочую папку и ищет в ней нужный файл bat
    :param path_work: str рабочая папка которую обходим
    :param find_o: str файл которую ищем
    """
    for base_path, sub_path, files_in_path in os.walk(path_work):
        if find_o in files_in_path:
            list_dir_magaz.append(base_path)
        else:
            yield base_path

def gen_files_path_rdp(path_work: str, find_o: str, list_dir_magaz: list) -> Iterable[str]:
    """
    функция-генератор рекурсивно обходит рабочую папку и ищет в ней нужный файл rdp
    :param path_work: str рабочая папка которую обходим
    :param find_o: str файл которую ищем
    """
    for base_path, sub_path, files_in_path in os.walk(path_work):
        res = list(filter(re.fullmatch(find_o, map(str, files_in_path)))
        if find_o in files_in_path:
            list_dir_magaz.append(base_path)
        else:
            yield base_path

def main():
    i_path = 'D:\\Dostup_magazini\\'
    file_n = 'GS_magaz.BAT'
    list_dir_magaz = []
    for _ in gen_files_path(i_path, file_n, list_dir_magaz):
        pass
    file_rdp = r'\S*sbis\S*'
    for _ in gen_files_path(i_path, file_rdp, list_dir_magaz):
        pass

    print(list_dir_magaz)

if __name__ == '__main__':
    main()