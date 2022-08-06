import pyautogui
from sys import exit

pyautogui.PAUSE = 1.5
xy = pyautogui.position()
# pyautogui.alert('ййййй')
log_rdp = pyautogui.locateOnScreen('logon_rdp_darc.png')
if log_rdp is None:
    exit(0)
print(log_rdp)
pyautogui.leftClick(log_rdp[0] + 30, log_rdp[1] // 2, 1)
pyautogui.write('123')
pyautogui.press('enter')

while True:
    logon_sbis = pyautogui.locateOnScreen('logon_sbis.png')
    print(logon_sbis)
    if logon_sbis is not None:
        break
pyautogui.write('ADMIN')
pyautogui.press('enter')
pyautogui.write('FDNJRHFNBZ')
pyautogui.press('enter')

