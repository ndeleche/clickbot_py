# Import necessary modules
import pyautogui as bot
import time
import os 
import math

# Wait for 5 seconds to allow time for the user to switch to the desired window.
time.sleep(5)

# Provide the correct path to the GitHub program.
github_path = r'C:\Users\NDELECHE HAMIS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GitHub, Inc.\GitHub Desktop.lnk'

# Open the GitHub program using the startfile function.
os.startfile(github_path)

# Wait for 5 seconds to allow time for the GitHub program to load.
time.sleep(3)

# Move the mouse cursor to the specified location and perform a double-click action to open a repository.
bot.moveTo(1006, 282, 2)
bot.doubleClick()

# Wait for 5 seconds to allow time for the page to load.
time.sleep(5)

# Move the mouse cursor to the specified location and click the "Code" button.
bot.moveTo(1122, 19, 1)
bot.click()

# Wait for 5 seconds to allow time for the download to complete.
time.sleep(5)

# Move the mouse cursor to the specified location and perform a single-click action to open the terminal.
bot.moveTo(364, 13, 1)
bot.click()

# Wait for 2 seconds to allow time for the terminal to focus.
time.sleep(2)

# Move the mouse cursor to the specified location and perform a single-click action to create a new tab in the terminal.
bot.moveTo(398, 40, 1)
bot.moveTo(625, 60, 1)
bot.click()

# Wait for 3 seconds to allow time for the terminal to open.
time.sleep(3)

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

time.sleep(5)

#-1
bot.moveTo(500, 628, 2, bot.easeInBounce)
bot.click()
time.sleep(2)

# Move the mouse in a around
radius = 50
center_x = 492
center_y = 315
angle = 0

while angle <= math.pi*2:
    # Calculate the x and y coordinates of the current point on the circle
    x = center_x + math.sin(angle) * radius
    y = center_y + math.cos(angle) * radius
    
    # Move the mouse to the current point
    bot.moveTo(x, y, duration=0.25)
    
    # Increment the angle by 10 degrees
    angle += math.pi/18

# Move the mouse around like a human
bot.moveTo(center_x+10, center_y+10, duration=0.5)
bot.moveTo(center_x-10, center_y-10, duration=0.5)

# Rest for 3 seconds
time.sleep(3)

#-2
bot.moveTo(1250, 321, 2, bot.easeInBounce)
bot.click()
time.sleep(2)

# Move the mouse in a around
radius = 50
center_x = 152
center_y = 324
angle = 30

while angle <= math.pi*2:
    # Calculate the x and y coordinates of the current point on the circle
    x = center_x + math.sin(angle) * radius
    y = center_y + math.cos(angle) * radius
    
    # Move the mouse to the current point
    bot.moveTo(x, y, duration=0.25)
    
    # Increment the angle by 10 degrees
    angle += math.pi/18

# Move the mouse around like a human
bot.moveTo(center_x+10, center_y+10, duration=0.5)
bot.moveTo(center_x-10, center_y-10, duration=0.5)

# Rest for 3 seconds
time.sleep(3)

#-3
bot.moveTo(600, 628, 2, bot.easeInBounce)
bot.click()
time.sleep(2)

# Move the mouse in a around
radius = 50
center_x = 152
center_y = 324
angle = 30

while angle <= math.pi*2:
    # Calculate the x and y coordinates of the current point on the circle
    x = center_x + math.sin(angle) * radius
    y = center_y + math.cos(angle) * radius
    
    # Move the mouse to the current point
    bot.moveTo(x, y, duration=0.25)
    
    # Increment the angle by 10 degrees
    angle += math.pi/18

# Move the mouse around like a human
bot.moveTo(center_x+10, center_y+10, duration=0.5)
bot.moveTo(center_x-10, center_y-10, duration=0.5)

bot.moveTo(97, 464, 3)
bot.moveTo(164, 465,3)
# Rest for 3 seconds
time.sleep(3)

#-4
bot.moveTo(1225, 250, 2, bot.easeInBounce)
bot.click()
time.sleep(2)

# Move the mouse in a around
radius = 50
center_x = 480
center_y = 300
angle = 0

while angle <= math.pi*2:
    # Calculate the x and y coordinates of the current point on the circle
    x = center_x + math.sin(angle) * radius
    y = center_y + math.cos(angle) * radius
    
    # Move the mouse to the current point
    bot.moveTo(x, y, duration=0.25)
    
    # Increment the angle by 10 degrees
    angle += math.pi/18

# Move the mouse around like a human
bot.moveTo(center_x+10, center_y+10, duration=0.5)
bot.moveTo(center_x-10, center_y-10, duration=0.5)

bot.moveTo(382, 463, 3)
bot.moveTo(501, 453, 3)
# Rest for 3 seconds
time.sleep(3)

#-5
bot.moveTo(200, 660, 2, bot.easeInBounce)
bot.click()
time.sleep(2)

# Move the mouse in a circle
radius = 50
center_x = 904
center_y = 315
angle = 0

while angle <= math.pi*2:
    # Calculate the x and y coordinates of the current point on the circle
    x = center_x + math.sin(angle) * radius
    y = center_y + math.cos(angle) * radius
    
    # Move the mouse to the current point
    bot.moveTo(x, y, duration=0.25)
    
    # Increment the angle by 10 degrees
    angle += math.pi/18

# Move the mouse around like a human
bot.moveTo(center_x+10, center_y+10, duration=0.5)
bot.moveTo(center_x-10, center_y-10, duration=0.5)

# Rest for 3 seconds
time.sleep(3)

#-6
bot.moveTo(1067, 200, 2, bot.easeInBounce)
bot.click()
time.sleep(2)

# Move the mouse in a circle
radius = 50
center_x = 1336
center_y = 122
angle = 0

while angle <= math.pi*2:
    # Calculate the x and y coordinates of the current point on the circle
    x = center_x + math.sin(angle) * radius
    y = center_y + math.cos(angle) * radius
    
    # Move the mouse to the current point
    bot.moveTo(x, y, duration=0.25)
    
    # Increment the angle by 10 degrees
    angle += math.pi/18

# Move the mouse around like a human
bot.moveTo(center_x+10, center_y+10, duration=0.5)
bot.moveTo(center_x-10, center_y-10, duration=0.5)

# Rest for 3 seconds
time.sleep(3)

#-7
bot.moveTo(1331, 578, 2, bot.easeInBounce)
bot.click()
time.sleep(2)
