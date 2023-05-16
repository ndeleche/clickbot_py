import pyautogui as bot
import time

def find_ad():
    """
    This function looks for the ad on the screen and returns the region and center position if found.
    """
    region = None
    center = None
    ad_img = 'blackfriday-1.png'
    confidence = 0.8
    ad_loc = bot.locateOnScreen(ad_img, confidence=confidence)
    if ad_loc is not None:
        left, top, width, height = ad_loc
        region = (left, top, width, height)
        center_x = left + width // 2
        center_y = top + height // 2
        center = (center_x, center_y)
    return region, center

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
    region, center = find_ad()
    if region is not None:
        print('I can see it')
        click_ad(center)
    else:
        print('I cannot see it')
    time.sleep(0.5)
