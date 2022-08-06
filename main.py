import pyautogui
import win32api
# from sys import exit
# import os
# from typing import Iterable
# from find_connector_to_shops import gen_files_path
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
i_path = 'D:\\YandexDisk\\rdp\\Dostup_magazini\\ace\\Clients\\GS_magaz.BAT'
work_parh = 'D:\\YandexDisk\\rdp\\Dostup_magazini\\ace\\Clients\\'
win32api.ShellExecute(0, 'open', i_path, None, work_parh, 1)