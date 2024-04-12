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
            print(f"{GREEN}[+] Sent GET request to {url} (User-Agent: {user_agent}){ENDC}")
        except Exception as e:
            print(f"{RED}[-] Error sending GET request: {e}{ENDC}")

        try:
            user_agent = UserAgent().random
            headers = {'User-Agent': user_agent}
            response = requests.post(url, headers=headers)
            # Uncomment the line below if you want to print the response content
            # print(response.text)
            requests_sent += 1
            print(f"{GREEN}[+] Sent POST request to {url} (User-Agent: {user_agent}){ENDC}")
        except Exception as e:
            print(f"{RED}[-] Error sending POST request: {e}{ENDC}")

    print(f"Sent {requests_sent} HTTP requests to {url} in {duration} seconds.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Send HTTP requests to a specified URL for a specified duration.")
    parser.add_argument("url", type=str, help="The URL of the target website")
    parser.add_argument("duration", type=float, help="The duration in seconds for sending HTTP requests")
    args = parser.parse_args()

    # Call the function to send HTTP requests
    send_http_requests(args.url, args.duration)
