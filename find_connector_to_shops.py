import os
from typing import Iterable
import re


def gen_files_path(path_work: str, find_o: str, list_dir_magaz: list) -> Iterable[str]:
    """
    функция-генератор рекурсивно обходит рабочую папку и ищет в ней нужный файл
    собирает вместе путь до файла и сам файл
    :param path_work: str рабочая папка которую обходим
    :param find_o: str файл которую ищем
    """
    for base_path, sub_path, files_in_path in os.walk(path_work):
        for res in files_in_path:
            if re.fullmatch(find_o, res) is not None:
                list_dir_magaz.append(base_path + '\\' + res)
        else:
            yield base_path


def main():
    # i_path = 'D:\\Dostup_magazini\\'
    i_path = 'D:\\YandexDisk\\rdp\\Dostup_magazini'
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