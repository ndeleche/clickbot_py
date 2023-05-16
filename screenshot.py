import pyautogui as bot

# Locate the address bar using PyAutoGUI
def find_address_bar():
    # Take a screenshot of the screen
    screenshot = bot.screenshot()

    # Search for the address bar image
    address_bar_image = bot.locateOnScreen('address_bar.png', confidence=0.8, grayscale=True, region=(0, 0, screenshot.width, screenshot.height))

    if address_bar_image is not None:
        # Get the center coordinates of the address bar
        address_bar_center = bot.center(address_bar_image)
        print(f"Address bar found at: {address_bar_center}")
    else:
        print("Address bar not found")

# Call the function to find the address bar
find_address_bar()
