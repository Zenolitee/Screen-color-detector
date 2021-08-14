from pyautogui import*
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

#Title 1 Position: X: 551 Y: 602 RGB:(181, 185, 235)
#Title 2 Position: X: 624 Y: 602 RGB:(253,  18,   1)
#Title 3 Position: X: 728 Y: 602 RGB:(180, 184, 234)
#Title 4 Position: X: 821 Y: 602 RGB:(169, 173, 232)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')== False:

    if pyautogui.pixel(547, 312)[0] == 0:
        click(547, 312)
    if pyautogui.pixel(626, 312)[0] == 0:
        click(626, 312)
    if pyautogui.pixel(741, 312)[0] == 0:
        click(741, 312)
    if pyautogui.pixel(801, 312)[0] == 0:
        click(801, 312)

   










        
    
