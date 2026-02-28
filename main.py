import requests
import time

def check_api(url):
    print(f"\nChecking API: {url}")
    
    start_time = time.time()
    try:
        response = requests.get(url)
        response_time = time.time() - start_time

        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")

        if response.status_code == 200:
            print("API is healthy ✅")
        else:
            print("API returned an unexpected status ⚠️")

    except requests.exceptions.RequestException as e:
        print("API request failed ❌")
        print(str(e))

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    check_api(url)