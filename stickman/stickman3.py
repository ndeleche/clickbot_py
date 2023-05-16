import pyautogui as bot
import time

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
