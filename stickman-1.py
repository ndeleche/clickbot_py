import requests
import time


time.sleep(5)

url = "http://127.0.0.1:8000/"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("URL is reachable and returns a 200 code")
            break
        else:
            print(f"URL returned a {response.status_code} code")
    except requests.exceptions.RequestException as e:
        print("URL is not reachable:", e)

    attempts += 1

    if attempts == max_attempts:
        print("Maximum number of attempts reached.")