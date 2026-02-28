import requests
import time


def check_api(api):
    print(f"\nChecking API: {api['name']}")
    print(f"URL: {api['url']}")

    start_time = time.time()

    result = {
        "healthy": False,
        "slow": False,
        "failed": False
    }

    try:
        response = requests.get(api["url"])
        response_time = time.time() - start_time

        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")

        if response.status_code == 200:
            print("Status: OK ✅")
            result["healthy"] = True
        else:
            print("Status: Unexpected response ⚠️")

        if response_time > api["max_response_time"]:
            print("Performance: Slow response ❌")
            result["slow"] = True
        else:
            print("Performance: Within acceptable limit 🚀")

    except requests.exceptions.RequestException as e:
        print("API request failed ❌")
        print(str(e))
        result["failed"] = True

    return result