import pyautogui as bot
import time
import os

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

# Wait for 5 seconds to allow time for the GitHub program to load.
wait(5)

# Open a repository by performing a double-click action at the specified location.
double_click_position(1006, 282)

# Wait for 5 seconds to allow time for the page to load.
wait(5)

# Wait for 5 seconds to allow time for the download to complete.
wait(5)

# Open the terminal by performing a single-click action at the specified location.
click_position(364, 13)

# Wait for 2 seconds to allow time for the terminal to focus.
wait(2)

# Create a new tab in the terminal.
click_position(398, 40)
click_position(625, 60)

# Wait for 3 seconds to allow time for the terminal to open.
wait(3)

# Activate the virtual environment by performing a single-click action at the specified location.
click_position(1100, 130)

# Wait for 3 seconds.
wait(3)

# Type the necessary commands in the terminal to start the Django server.
type_text('cd ecommerce\n')
type_text('py manage.py runserver\n')

# Wait for 2 seconds.
wait(2)

# Open the web browser by performing a single-click action at the specified location.
click_position(129, 745)

# Wait for 2 seconds and open Google Chrome.
wait(2)
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
wait(2)


def find_ads():
    """
    This function looks for ads on the screen and returns a list of regions and center positions if found.
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
            ads.append((region, center))
    return ads

def click_ad(center):
    """
    This function moves the cursor towards the center position and clicks the ad.
    """
    if center is not None:
        bot.moveTo(center[0], center[1], duration=1.5)
        bot.click()
        time.sleep(2)

# Wait for 2 seconds before starting
time.sleep(2)

while True:
    ads = find_ads()
    if ads:
        print(f"I can see {len(ads)} ad(s)")
        for ad in ads:
            region, center = ad
            click_ad(center)
            time.sleep(1)
    else:
        print('I cannot see any ads')
    time.sleep(0.5)
