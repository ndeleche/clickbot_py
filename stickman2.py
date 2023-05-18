"""
            CLICK-BOT
"""
# Import necessary modules
import pyautogui as bot
import random
import time
import os 
import requests

def wait(seconds):
    time.sleep(seconds)

def open_program(path):
    os.startfile(path)

def click_position(x, y, duration=2):
    bot.moveTo(x, y, duration=duration)
    bot.click()

def double_click_position(x, y, duration=2):
    bot.moveTo(x, y, duration=duration)
    bot.doubleClick()

def type_text(text, interval=0.1):
    bot.write(text, interval=interval)

# Wait for 5 seconds to allow time for the user to switch to the desired window.
wait(5)

# Provide the correct path to the GitHub program.
github_path = r'C:\Users\NDELECHE HAMIS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GitHub, Inc.\GitHub Desktop.lnk'

# Open the GitHub program using the startfile function.
open_program(github_path)

# Wait for 8 seconds to allow time for the GitHub program to load.
wait(8)

# Open a repository by performing a double-click action at the specified location.
double_click_position(1006, 282)

# Wait for 5 seconds to allow time for the page to load.
wait(10)

# Open the terminal by performing a single-click action at the specified location.
click_position(364, 13)

# Wait for 4 seconds to allow time for the terminal to focus.
wait(4)

# Create a new tab in the terminal.
click_position(398, 40)
click_position(625, 60)

# Wait for 5 seconds to allow time for the terminal to open.
wait(5)

# Activate the virtual environment by performing a single-click action at the specified location.
click_position(1100, 130)

# Wait for 5 seconds.
wait(5)

# Type the necessary commands in the terminal to start the Django server.
type_text('cd ecommerce\n')
type_text('py manage.py runserver\n')

# Wait for  seconds.
wait(5)

# Open the web browser by performing a single-click action at the specified location.
click_position(129, 745)

# Wait for 3 seconds and open Google Chrome.
wait(3)
type_text('chrome')

# Click on the address bar.
click_position(462, 361)

# Wait for 4 seconds.
wait(4)

# Open a new tab.
click_position(704, 453)

# Wait for 2 seconds and click on the address bar.
wait(2)
click_position(325, 57)

# Type the URL of the local server and press Enter to access the website.
type_text("http://127.0.0.1:8000/")
wait(3)
bot.press('enter')

# Wait for 10 seconds.
wait(10)

# Define the start and end points for dragging.
start_point = (1355, 155)
end_point = (1356, 370)

# Move the cursor to the start point.
bot.moveTo(start_point, duration=1)

# Perform the hold and drag action.
bot.mouseDown()
bot.dragTo(end_point, duration=2)
bot.mouseUp()

# Wait for a moment before continuing.
wait(10)

url = "http://127.0.0.1:8000/"
def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("URL is reachable and returns a 200 code")
        else:
            print(f"URL returned a {response.status_code} code")
    except requests.exceptions.RequestException as e:
        print("URL is not reachable:", e)

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
        check_url(url)  # Request the URL after clicking the ad

        # Store the center position, region, and ad name in a file or database
        # You can modify this part to store the data as per your requirement

# Wait for 2 seconds before starting
time.sleep(2)

# URL checking before detecting ads and clicking
check_url(url)

# Wait for 1 minute (60 seconds) between ad clicks
ad_wait_time = 60

# Track clicked ads
clicked_ads = set()

while True:
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
