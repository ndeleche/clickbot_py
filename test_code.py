import requests

def check_user_agent(url, user_agent):
    headers = {
        'User-Agent': user_agent
    }
    consistent_responses = set()  # To store consistent responses
    
    try:
        for _ in range(1):  # Sending ten requests
            response = requests.get(url, headers=headers, timeout=5)  # Increased timeout to 5 seconds
            
            if response.status_code == 200:
                consistent_responses.add(response.content)
            else:
                print("User-Agent is either invalid or detected as a bot.")
                return
            
        if len(consistent_responses) == 1:
            print("User-Agent is valid and not detected as a bot.")
        else:
            print("User-Agent is detected as a bot due to inconsistent responses.")
    
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the request:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))

# Example usage
url = 'http://iamndeleche.pythonanywhere.com/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

check_user_agent(url, user_agent)
