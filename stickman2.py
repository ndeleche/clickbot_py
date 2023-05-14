from pyautogui import *
import pyautogui as bot
import random
import keyboard
import time
import win32api, win32con

# Dictionary of ads to detect, with corresponding names
ads = {
    'blackfriday-1.png': 'Ad 1',
    'blackfriday-2.png': 'Ad 2',
    'blackfriday-3.png': 'Ad 3',
    'blackfriday-4.png': 'Ad 4'
}

time_to_wait = 600 # in seconds, i.e. 10 minutes
last_detection_time = time.time() - time_to_wait # so it will trigger the first time

# Function to detect ads on the webpage and move the cursor to them
def detect_ads():
    global last_detection_time
    
    # Check if the webpage is active
    is_webpage_active = bot.locateOnScreen('webpage.png', confidence=0.8)
    if is_webpage_active is None:
        print('Webpage not active. Bot stopped.')
        return
    
    # Print message and wait if it's time for a new search
    current_time = time.time()
    if current_time - last_detection_time >= time_to_wait:
        last_detection_time = current_time
        print('Starting new search...')
        time.sleep(5) # wait for webpage to fully load
    
    # Create dictionary to store ad regions and centers, and a list of ads to detect
    ads_to_detect = ads.copy()
    detected_ads = {}
    
    # Loop through ads until all have been detected
    while ads_to_detect:
        # Randomly select an ad to detect
        filename, ad_name = random.choice(list(ads_to_detect.items()))
        location = bot.locateOnScreen(filename, confidence=0.8)
        if location is not None:
            # If ad is detected, store its region and center positions, and remove it from list of ads to detect
            print(f'Found {ad_name} at {location}')
            center = bot.center(location)
            region = (center[0]-50, center[1]-50, 100, 100)
            detected_ads[ad_name] = {'region': region, 'center': center}
            print(f'Center position of {ad_name} is {center}')
            print(f'Region of {ad_name} is {region}')
            bot.moveTo(center[0] + random.randint(-50, 50), center[1] + random.randint(-50, 50))
            ads_to_detect.pop(filename)
        else:
            print(f'Could not find {ad_name}')
    
    # Click on all detected ads in random order
    ad_names = list(detected_ads.keys())
    random.shuffle(ad_names)
    for ad_name in ad_names:
        ad = detected_ads[ad_name]
        bot.moveTo(ad['center'])
        bot.click()
        time.sleep(2) # wait for ad to load
        
    # Wait for random time before starting a new search
    wait_time = random.randint(120, 300) # in seconds
    print(f'Waiting {wait_time} seconds before starting new search...')
    time.sleep(wait_time)

# Start the bot in a continuous loop
while True:
    detect_ads()
