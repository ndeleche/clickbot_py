                                                         REQUIREMENT

-Text editor 

-python  3.11.1





Python script that simulates a click bot. It uses the pyautogui library to automate mouse movements and clicks on the screen. Here's a breakdown of the script:

                                                       NECESSARY MODULES:

-pyautogui for automation,

-random for generating random values,

-time for time-related functions,

-os for operating system-related functions, and 

-requests for sending HTTP requests.




                                               HOW TO INSTALL THE REQUIRED MODULES:

for the Python code to work, you can use the pip package manager, which is the standard package manager for Python. Here are the installation commands for each module:

NOTE:
you can install using your command prompt or terminal on your vscode if your using it or pycharm ect.


1.PYAUTOGUI


![pyuatogui (3)](https://github.com/ndeleche/clickbot_py/assets/80362168/43a6572b-2381-4051-8a6e-0f48c2177767)

2.REQUESTS  


![request](https://github.com/ndeleche/clickbot_py/assets/80362168/6e377a91-838e-42f4-a2c4-15f4dd36c0e8)


3.OS, RANDOM, TIME 

-Both modules are  part of Python's standard library and does not require a separate installation.



                                                            FLOW CHART OF THE BOT 



COMING SOON 

EXPLANATION OF IT HOW IT WORKS 












The script defines several functions for different actions, such as waiting for a specified duration, opening a program, clicking at a specific position, typing text, and pressing the Enter key.

It waits for 5 seconds initially using the wait() function.

It opens the web browser by performing a single-click action at the specified location.

After waiting for 3 seconds, it types 'chrome' in the address bar.

It clicks on the address bar and waits for 4 seconds.

It opens a new tab by clicking at the specified position.

After waiting for 2 seconds, it clicks on the address bar of the new tab.

It types the URL of a local server and presses Enter to access the website.

It waits for 10 seconds.

It defines the start and end points for dragging and performs the hold and drag action.

It waits for 10 seconds again.

It defines a URL to check its reachability.

It defines a function check_url() that sends an HTTP GET request to the URL and checks the response status code.

It defines a loop function url_check_loop() that repeatedly checks the URL using the check_url() function every 10 seconds.

It creates a thread to run the URL check loop in the background.

It defines a function find_ads() that searches for ads on the screen and returns their regions, center positions, and names.

It defines a function click_ad() that moves the cursor towards the ad's center position and clicks it.

It enters an infinite loop that continuously checks the URL's reachability and looks for ads to click.

If the URL is not reachable, it sleeps for 10 seconds before checking again.

If ads are found, it clicks on each ad that hasn't been clicked before, waits for a random amount of time, and then performs a random movement.

If no ads are found, it sleeps for a short duration before checking again.


                                                       HOW TO RUN THE SCRIPT 


click the Run Python File in Terminal play button in the top-right side of the editor(vscode)
