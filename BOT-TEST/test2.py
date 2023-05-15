import pyautogui as bot
import time
time.sleep(5)

start_point = bot.Point(1355, 155)
end_point = bot.Point(1356, 370)

# Move the cursor to the start point
bot.moveTo(start_point, duration=0.5)

# Perform the hold and drag action
bot.mouseDown()
bot.dragTo(end_point, duration=2)
bot.mouseUp()

# Wait for a moment before continuing
time.sleep(2)
