# Import necessary modules
import pyautogui as bot
import random
import time
import os 
import requests
from threading import Thread

def wait(seconds):
    time.sleep(seconds)
    
def open_chrome():
    # Check the operating system to determine the appropriate command to open Chrome
    if os.name == 'nt':  # For Windows
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
  # else:
       # print("Unsupported operating system")

def click_position(x, y, duration=0.01):
    bot.moveTo(x, y, duration=duration)
    bot.click()

def double_click_position(x, y, duration=0.01):
    bot.moveTo(x, y, duration=duration)
    bot.doubleClick()

def type_text(text, interval=0.1):
    bot.write(text, interval=interval)

def press_enter():
    bot.press('enter')
     
def refresh_page():
    bot.press('F5')
       
# Wait for  seconds.
wait(2)

open_chrome()

# Wait for 2 seconds.
wait(1)

# Open a new tab.
click_position(704, 453)

# Wait for 2 seconds and click on the address bar.
wait(1)

click_position(325, 57)

# Type the URL of the local server and press Enter to access the website.
type_text("http://iamndeleche.pythonanywhere.com/")

wait(1)

press_enter()

# Wait for 2seconds.
wait(1)

# Define the start and end points for dragging.
start_point = (1355, 155)

end_point = (1357, 436)

# Move the cursor to the start point.
bot.moveTo(start_point, duration=1)

# Perform the hold and drag action.
bot.mouseDown()

bot.dragTo(end_point, duration=0.2)

bot.mouseUp()

# Wait for a moment before continuing.
wait(1)

url = "http://iamndeleche.pythonanywhere.com/"

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("server is reachable ")
            return True
        else:
            print(f"URL returned a {response.status_code} code")
    except requests.exceptions.RequestException as e:
        print("server is not reachable:", e)
    return False

def url_check_loop():
    while True:
        if check_url(url):
            break
        time.sleep(5)  # Wait for 10 seconds before the next URL check

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
        bot.moveTo(center[0], center[1], duration=0.2)
        bot.click()
        time.sleep(2)
        print(f"Clicked ad: {ad_name}")
        print(f"Position: {center}")
        
        # Request the URL after clicking the ad
        check_url(url)

        # Store the center position, region, and ad name in a file or database
        # You can modify this part to store the data as per your requirement

# Wait for 2 seconds before starting
time.sleep(1)

# Wait for 15 seconds(30 seconds) between ad clicks
ad_wait_time = 2

# Track clicked ads
clicked_ads = set()

while True:
    if not check_url(url):
        print("Am sleeping until server is reachable...")
        time.sleep(1)  # Sleep for 10 seconds before checking the URL again
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
                move_distance = random.randint(200, 500)
                move_direction = random.choice(['left', 'right', 'up', 'down'])
                if move_direction == 'left':
                    bot.move(-move_distance, 0, duration=0.1)
                elif move_direction == 'right':
                    bot.move(move_distance, 0, duration=0.1)
                elif move_direction == 'up':
                    bot.move(0, -move_distance, duration=0.1)
                elif move_direction == 'down':
                    bot.move(0, move_distance, duration=.1)
                # Randomize wait time before the next ad click
                time.sleep(random.randint(ad_wait_time - 30, ad_wait_time + 30))
    else:
        # print('I cannot see any ad')
        time.sleep(0.2)