import time
import random
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = "http://iamndeleche.pythonanywhere.com/"
ad_images = ['blackfriday-1.png', 'blackfriday-2.png', 'blackfriday-3.png', 'blackfriday-4.png']
ad_wait_time = 30
clicked_ads = set()

def url_check_loop():
    while True:
        driver.refresh()
        time.sleep(5)  # Wait for 5 seconds before the next URL check

def find_ads():
    """
    This function looks for ads on the screen and returns a list of regions, center positions, and ad names if found.
    """
    ads = []
    for ad_img in ad_images:
        if driver.find_element_by_xpath(f"//img[contains(@src, '{ad_img}')]"):
            ad_element = driver.find_element_by_xpath(f"//img[contains(@src, '{ad_img}')]")
            region = ad_element.location
            size = ad_element.size
            center_x = region['x'] + size['width'] // 2
            center_y = region['y'] + size['height'] // 2
            center = (center_x, center_y)
            ad_name = ad_img.split('.')[0]
            ads.append((region, center, ad_name))
    return ads

def click_ad(center, ad_name):
    """
    This function moves the cursor towards the center position and clicks the ad.
    """
    if center is not None:
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), center[0], center[1])
        actions.click()
        actions.perform()
        time.sleep(2)
        print(f"Clicked ad: {ad_name}")
        print(f"Position: {center}")

        # Store the center position, region, and ad name in a file or database
        # You can modify this part to store the data as per your requirement

# Create a Selenium WebDriver instance (modify according to your preferred browser and its WebDriver)
driver = webdriver.Chrome()

# Open the URL in the browser
driver.get(url)

# Create and start the URL check thread
url_check_thread = Thread(target=url_check_loop)
url_check_thread.start()

while True:
    ads = find_ads()
    if ads:
        for ad in ads:
            region, center, ad_name = ad
            if ad_name not in clicked_ads:
                click_ad(center, ad_name)
                clicked_ads.add(ad_name)
                # Randomize movement after clicking an ad
                move_distance = random.randint(200, 500)
                move_direction = random.choice(['left', 'right', 'up', 'down'])
                if move_direction == 'left':
                    driver.execute_script(f"window.scrollBy(-{move_distance}, 0)")
                elif move_direction == 'right':
                    driver.execute_script(f"window.scrollBy({move_distance}, 0)")
                elif move_direction == 'up':
                    driver.execute_script(f"window.scrollBy(0, -{move_distance})")
                elif move_direction == 'down':
                    driver.execute_script(f"window.scrollBy(0, {move_distance})")
                # Randomize wait time before the next ad click
                time.sleep(random.randint(ad_wait_time - 30, ad_wait_time + 30))
    else:
        time.sleep(0.2)

# Close the browser
driver.quit()
