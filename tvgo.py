import pyautogui
import time

#size
print(pyautogui.size())
sizeX = 1280
sizeY = 720

def halfScreen(): 
    percentX = sizeX-(sizeX*0.5)
    percentY = sizeY-(sizeY*0.5)
    return percentX, percentY

def calculateUbicationButtonFullSize():
    percentX = sizeX-(sizeX*0.093)
    percentY = sizeY-(sizeY*0.082)
    return percentX, percentY

pyautogui.hotkey('win', 'r')
time.sleep(1.5)
pyautogui.write('chrome.exe "https://tvgo.americatv.com.pe/"', interval=0.01)
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(3)

#click - X and Y
pyautogui.click(halfScreen())
time.sleep(2)
#scroll down sizeY-(sizeY*0.5)-20
pyautogui.scroll(-340)
time.sleep(2)

#0.093  0.95% -- x
#0.082  0.85% -- y
pyautogui.click(calculateUbicationButtonFullSize())
time.sleep(0.5)
pyautogui.moveTo(halfScreen())