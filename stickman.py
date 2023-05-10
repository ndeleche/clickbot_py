from pyautogui import *
import pyautogui as bot
import random
import keyboard
import time

images = {
    'blackfriday-1.png': 'Type 1',
    'blackfriday-2.png': 'Type 2',
    'blackfriday-3.png': 'Type 3',
    'blackfriday-4.png': 'Type 4'
}

time_to_wait = 600  # in seconds, i.e. 10 minutes
last_detection_time = time.time() - time_to_wait  # so it will trigger the first time
mouse_speed = 10  # adjust as needed

while True:
    current_time = time.time()
    if current_time - last_detection_time >= time_to_wait:
        last_detection_time = current_time
        print('Starting new search...')
        for i in range(3):  # move the mouse around randomly to simulate human use
            x, y = position()
            x += random.randint(-mouse_speed, mouse_speed)
            y += random.randint(-mouse_speed, mouse_speed)
            moveTo(x, y, duration=random.uniform(0.5, 1.5))
            time.sleep(random.uniform(0.5, 1.5))

    images_to_detect = images.copy()
    while images_to_detect:
        for filename, image_type in images_to_detect.items():
            location = bot.locateOnScreen(filename, confidence=0.8)
            if location is not None:
                print(f'Found {image_type} image at {location}')
                center = bot.center(location)
                print(f'Center position of {image_type} image is {center}')
                region = (center[0]-50, center[1]-50, 100, 100)
                print(f'Region of {image_type} image is {region}')
                bot.moveTo(center[0] + random.randint(-50, 50), center[1] + random.randint(-50, 50),
                            duration=random.uniform(0.5, 1.5))  # move the mouse around randomly to simulate human use
                time.sleep(random.uniform(0.5, 1.5))
                images_to_detect.pop(filename)
                break
        else:
            print('Could not find any more images')
            break

    time.sleep(0.5)

    # check for keyboard input to stop/start the bot
    if keyboard.is_pressed('q'):
        print('Quitting...')
        break
    elif keyboard.is_pressed('w'):
        print('Starting new search...')
        last_detection_time = time.time() - time_to_wait  # trigger a new search immediately
        time.sleep(2)  # wait a bit to avoid accidentally triggering another search
