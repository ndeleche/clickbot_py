import requests
import time
import pyautogui as bot
import random
from threading import Thread

url = "http://127.0.0.1:8000/"

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("URL is reachable and returns a 200 code")
            return True
        else:
            print(f"URL returned a {response.status_code} code")
    except requests.exceptions.RequestException as e:
        print("URL is not reachable:", e)
    return False

def url_check_loop():
    while True:
        if check_url(url):
            break
        time.sleep(10)  # Wait for 10 seconds before the next URL check

# Create and start the URL check thread
url_check_thread = Thread(target=url_check_loop)
url_check_thread.start()

def find_ads():
    """
    This function looks for ads on the screen and returns a list of regions, center positions, and ad names if found.
    """
    ads = []
    ad_images = ['blackfriday-1.png', 'blackfriday-2.png', 'blackfriday-3.png', 'blackfriday-4.png']
    confidence = 0.8
    for ad_img in ad_images:
        ad_loc = bot.locateOnScreen(ad_img, confidence=confidence)
        if ad_loc is not None:
            left, top, width, height = ad_loc
            region = (left, top, width, height)
            center_x = left + width // 2
            center_y = top + height // 2
            center = (center_x, center_y)
            ad_name = ad_img.split('.')[0]
            ads.append((region, center, ad_name))
    return ads

def click_ad(center, ad_name):
    """
    This function moves the cursor towards the center position and clicks the ad.
    """
    if center is not None:
        bot.moveTo(center[0], center[1], duration=1.5)
        bot.click()
        time.sleep(2)
        print(f"Clicked ad: {ad_name}")

        # Request the URL after clicking the ad
        check_url(url)

        # Store the center position, region, and ad name in a file or database
        # You can modify this part to store the data as per your requirement

# Wait for 2 seconds before starting
time.sleep(2)

# Wait for 1 minute (60 seconds) between ad clicks
ad_wait_time = 60

# Track clicked ads
clicked_ads = set()

while True:
    if not check_url(url):
        print("Sleeping until the URL is reachable...")
        time.sleep(10)  # Sleep for 10 seconds before checking the URL again
        continue
    
    ads = find_ads()
    if ads:
        # print(f"I can see {len(ads)} ads")
        for ad in ads:
            region, center, ad_name = ad
            if ad_name not in clicked_ads:
                click_ad(center, ad_name)
                clicked_ads.add(ad_name)
                # Randomize movement after clicking an ad
                move_distance = random.randint(100, 300)
                move_direction = random.choice(['left', 'right', 'up', 'down'])
                if move_direction == 'left':
                    bot.move(-move_distance, 0, duration=2)
                elif move_direction == 'right':
                     bot.move(move_distance, 0, duration=2)
                elif move_direction == 'up':
                    bot.move(0, -move_distance, duration=2)
                elif move_direction == 'down':
                    bot.move(0, move_distance, duration=2)
                # Randomize wait time before the next ad click
                time.sleep(random.randint(ad_wait_time - 30, ad_wait_time + 30))
    else:
        # print('I cannot see any ad')
        time.sleep(0.5)
 