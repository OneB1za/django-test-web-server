
import requests
import time

def make_requests():
    urls = [
        "http://127.0.0.1:8000/slow/",
        "http://127.0.0.1:8000/usual/",
        "http://127.0.0.1:8000/random/",
        #"http://127.0.0.1:8000/",
    ]

    while True:
        for url in urls:
            try:
                response = requests.get(url, timeout=10)
                print \
                    (f"Request to {url}: {response.status_code} | {response.text[:35]}")
            except requests.RequestException as e:
                print(f"Something went wrong: {url}: {e}")

        time.sleep(0.3)

if __name__ == "__main__":
    print("Started...")
    make_requests()