import pyautogui
import win32api
from sys import exit
import os
from typing import Iterable
from find_connector_to_shops import gen_files_path
from decouple import config as conf_token
#
# pyautogui.PAUSE = 1.5
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

def find_all_path():
    # i_path = 'D:\\Dostup_magazini\\'
    i_path = 'D:\\YandexDisk\\rdp\\Dostup_magazini'
    file_n = 'GS_magaz.BAT'
    list_dir_magaz = []
    for _ in gen_files_path(i_path, file_n, list_dir_magaz):
        pass
    file_rdp = r'\S*sbis\S*'
    for _ in gen_files_path(i_path, file_rdp, list_dir_magaz):
        pass
    return list_dir_magaz

# all_path_to_sbis = find_all_path()
# print(all_path_to_sbis)
sbis_login = conf_token('sbis_login', default=None)
sbis_pass = conf_token('sbis_pass', default=None)
win_login = conf_token('rdp_login', default=None)
win_pass = conf_token('rdp_pass', default=None)
print(sbis_login)
print(sbis_pass)
print(win_login)
print(win_pass)