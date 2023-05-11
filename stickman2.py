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

time_to_wait = 600 # in seconds, i.e. 10 minutes
last_detection_time = time.time() - time_to_wait # so it will trigger the first time
move_time = 0.5 # in seconds, i.e. move the cursor for half second

while True:
    current_time = time.time()
    if current_time - last_detection_time >= time_to_wait:
        last_detection_time = current_time
        print('Starting new search...')
        bot.moveTo(random.randint(100, 500), random.randint(100, 500), duration=move_time)
        time.sleep(move_time)
        bot.scroll(random.randint(-2, 2))
        time.sleep(move_time)
        bot.moveTo(random.randint(100, 500), random.randint(100, 500), duration=move_time)
        time.sleep(move_time)

    images_to_detect = list(images.items())
    random.shuffle(images_to_detect)
    while images_to_detect:
        filename, image_type = images_to_detect.pop()
        location = bot.locateOnScreen(filename, confidence=0.8)
        if location is not None:
            print(f'Found {image_type} image at {location}')
            center = bot.center(location)
            print(f'Center position of {image_type} image is {center}')
            region = (center[0]-50, center[1]-50, 100, 100)
            print(f'Region of {image_type} image is {region}')
            bot.moveTo(center[0] + random.randint(-50, 50), center[1] + random.randint(-50, 50), duration=move_time)
            bot.scroll(random.randint(-2, 2))
            time.sleep(move_time)
            break
    else:
        print('Could not find any more images')
        bot.moveTo(random.randint(100, 500), random.randint(100, 500), duration=move_time)
        time.sleep(move_time)
