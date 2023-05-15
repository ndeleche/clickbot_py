from pyautogui import *
import pyautogui as bot
import random
import keyboard
import time
import win32api, win32con

time.sleep(2)
while 1:
    if bot.locateOnScreen('stickman.png', confidence= 0.8) != None:
        print('I can see it')
        time.sleep(0.5)
    else:
        print('I cannot see it')
        time.sleep(0.5)