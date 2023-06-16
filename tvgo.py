import pyautogui
import time

#size
screen_width, screen_height = pyautogui.size()

def halfScreen(): 
    percentX = screen_width-(screen_width*0.5)
    percentY = screen_height-(screen_height*0.5)
    return percentX, percentY

pyautogui.hotkey('win', 'r')
time.sleep(1.5)
pyautogui.write('chrome.exe "https://tvgo.americatv.com.pe/"', interval=0.01)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(3)

#click - X and Y
pyautogui.click(halfScreen())
time.sleep(2)

if (screen_width == 1280) and (screen_height == 720):
    #scroll down sizeY-(sizeY*0.5)-20
    pyautogui.scroll(-340)
    time.sleep(2)
    #0.093  0.95% -- x
    #0.082  0.85% -- y
    pyautogui.click(1160, 660)

elif (screen_width == 1600) and (screen_height == 900):
    pyautogui.scroll(-348)
    time.sleep(2)
    pyautogui.click(1500, 820)

elif (screen_width == 1920) and (screen_height == 1080):
    pyautogui.scroll(-355)
    time.sleep(2)
    pyautogui.click(1800, 1000)

time.sleep(1.5)
pyautogui.moveTo(halfScreen())
time.sleep(0.5)
pyautogui.moveTo(halfScreen())