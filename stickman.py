from pyautogui import *
import pyautogui as bot
import random
import keyboard
import time
import win32api, win32con

time.sleep(2)
while 1:
    if bot.locateOnScreen('stickman.png') != none:
        print('I can see it')
        time.sleep(0.5)
    else:
        print('I cannot see it')
        time.sleep(0.5)