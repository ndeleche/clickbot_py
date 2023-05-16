from pyautogui import *
import pyautogui as bot
import time

def check_image_loop(image_path, confidence=0.8):
    while True:
        if bot.locateOnScreen(image_path, confidence=confidence) is not None:
            print("I can see it")
        else:
            print("I cannot see it")
        time.sleep(0.5)

# Delay before starting the loop
time.sleep(2)

# Call the function with the image path and confidence level
check_image_loop('blackfriday-1.png', confidence=0.8)
