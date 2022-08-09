import pyautogui
import win32api
from sys import exit
import os
from typing import Iterable
from find_connector_to_shops import gen_files_path
from decouple import config as conf_token
#
pyautogui.PAUSE = 1.5
# xy = pyautogui.position()
# log_rdp = pyautogui.locateOnScreen('logon_rdp_darc.png')
# if log_rdp is None:
#     exit(0)
# print(log_rdp)
# pyautogui.leftClick(log_rdp[0] + 30, log_rdp[1] // 2, 1)
# pyautogui.write('123')
# pyautogui.press('enter')
#
# while True:
#     logon_sbis = pyautogui.locateOnScreen('logon_sbis.png')
#     print(logon_sbis)
#     if logon_sbis is not None:
#         break
# pyautogui.write('ADMIN')
# pyautogui.press('enter')
# pyautogui.write('FDNJRHFNBZ')
# pyautogui.press('enter')
#
# win32api.shel('D:\\YandexDisk\\rdp\\Dostup_magazini\\ace\\Clients\\GS_magaz.BAT')
# i_path = 'D:\\YandexDisk\\rdp\\Dostup_magazini\\ace\\Clients\\GS_magaz.BAT'
# work_parh = 'D:\\YandexDisk\\rdp\\Dostup_magazini\\ace\\Clients\\'
# win32api.ShellExecute(0, 'open', i_path, None, work_parh, 1)

def find_all_path_file(i_start_path: str, i_file: str, i_list_path) -> None:
    """
    вызов генератор для перебора папок
    :param i_start_path: str путь с котрого начинаем
    :param i_file: str файл который ищем
    :param i_list_path: list списко путей где мы нашли наш файл
    """
    for _ in gen_files_path(i_start_path, i_file, i_list_path):
        pass

def find_all_path(i_list: list) -> list:
    """
    функция перебора стартовой папки
    для поиска в ней файлов из входного списка
    :param i_list: list список имен файлов которые ищем
    :return: list список путей где мы встретили наши файлы
    """
    # i_path = 'D:\\Dostup_magazini\\'
    i_path = 'D:\\YandexDisk\\rdp\\Dostup_magazini'
    list_dir_magaz = []
    for i_file_name in i_list:
        find_all_path_file(i_path, i_file_name, list_dir_magaz)
    return list_dir_magaz


def connect_to_georgia(i_path: str, work_path: str):
    """
    функция подключения к джорджии
    :param i_path: str путь запуска
    :param work_path: str рабочая папка запуска
    :return:
    """
    win32api.ShellExecute(0, 'open', i_path, None, work_path, 1)
    pass


def connect_to_rdp(i_path: str, work_path: str):
    """
    функция подключения сначала к ремоутапп
    :param i_path: str путь запуска приложения
    :param work_path: str рабочая папка
    :return:
    """
    win32api.ShellExecute(0, 'open', i_path, None, work_path, 1)
    pass


def connect_to_mag(i_list_path: list):
    """
    функция перебора нашего списка с коннекторами к сбису
    и вызов этих коннекторов
    :param i_list_path:
    :return:
    """
    for i_path in i_list_path:
        if os.path.exists(i_path):
            work_path, sep, work_file = i_path.rpartition('\\')
            if work_file.lower().endswith('.bat'):
                connect_to_georgia(i_path, work_path)
            else:
                connect_to_rdp(i_path, work_path)


list_f_name = ['GS_magaz.BAT', r'\S*sbis\S*']
# list_f_name = [r'\S*sbis\S*']
all_path_to_sbis = find_all_path(list_f_name)
connect_to_mag(all_path_to_sbis)
print(all_path_to_sbis)

sbis_login = conf_token('sbis_login', default=None)
sbis_pass = conf_token('sbis_pass', default=None)
win_login = conf_token('rdp_login', default=None)
win_pass = conf_token('rdp_pass', default=None)
print(sbis_login)
print(sbis_pass)
print(win_login)
print(win_pass)