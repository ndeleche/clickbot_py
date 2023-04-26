# Import necessary modules

import pyautogui as bot
import time
import os 
import random

# Wait for 5 seconds to allow time for the user to switch to the desired window.
time.sleep(5)

# Provide the correct path to the GitHub program.
github_path = r'C:\Users\NDELECHE HAMIS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GitHub, Inc.\GitHub Desktop.lnk'

# Open the GitHub program using the startfile function.
os.startfile(github_path)

# Wait for 5 seconds to allow time for the GitHub program to load.
time.sleep(5)

# Move the mouse cursor to the specified location and perform a double-click action to open a repository.
bot.moveTo(1006, 282, 4)
bot.doubleClick()

# Wait for 5 seconds to allow time for the page to load.
time.sleep(5)

# Move the mouse cursor to the specified location and click the "Code" button.
bot.moveTo(1122, 19, 4)
bot.click()

# Wait for 3 seconds.
time.sleep(3)

# Click the "Download ZIP" button.
bot.click()

# Wait for 5 seconds to allow time for the download to complete.
time.sleep(5)

# Move the mouse cursor to the specified location and perform a single-click action to open the terminal.
bot.moveTo(364, 13, 4)
bot.click()

# Wait for 5 seconds to allow time for the terminal to focus.
time.sleep(4)

# Move the mouse cursor to the specified location and perform a single-click action to create a new tab in the terminal.
bot.moveTo(398, 40, 2)
bot.moveTo(625, 60, 2)
bot.click()

# Wait for 5 seconds to allow time for the terminal to open.
time.sleep(4)

# Move the mouse cursor to the specified location and perform a single-click action to activate the virtual environment.
bot.moveTo(1100, 130, 3)
bot.click()

# Wait for 3 seconds.
time.sleep(3)

# Type the necessary commands in the terminal to start the Django server.
bot.typewrite('cd ecommerce\n', interval=0.1)
bot.typewrite('py manage.py runserver\n', interval=0.1)

# Wait for 2 seconds.
time.sleep(2)

# Move the mouse cursor to the specified location and perform a single-click action to open the web browser.
bot.moveTo(129, 745, 2)
bot.click(184, 755, 2)

# Wait for 2 seconds and type "chrome" to open Google Chrome.
time.sleep(2)
bot.write('chrome')

# Move the mouse cursor to the specified location and click on the address bar.
bot.moveTo(462, 361, 2)
bot.click(462, 361, 2)

# Wait for 4 seconds.
time.sleep(4)

# Move the mouse cursor to the specified location and click on the new tab button.
bot.moveTo(704, 453, 2)
bot.click(704, 453, 2)

# Wait for 2 seconds and click on the address bar.
time.sleep(2)
bot.moveTo(325, 57, 2)
bot.click()

# Type the URL of the local server and press Enter to access the website.
bot.write("http://127.0.0.1:8000/")
time.sleep(3)
bot.press('enter')


# Set the duration of the movement to 5 seconds
duration = 5

# Get the size of the screen
screen_width, screen_height = bot.size()

# Get the current position of the cursor
current_x, current_y = bot.position()

# Set the start time
start_time = time.time()

# Move the cursor randomly for 5 seconds
while (time.time() - start_time) < duration:
    # Generate random coordinates for the new position of the cursor
    new_x = random.randint(0, screen_width)
    new_y = random.randint(0, screen_height)

    # Move the cursor to the new position
    bot.moveTo(new_x, new_y, duration=0.5)
    
    # Pause for a short period of time before moving to the next position
    time.sleep(0.5)
    
# Move the cursor back to the original position
bot.moveTo(current_x, current_y, duration=0.5)

bot.click(613, 630, 3)