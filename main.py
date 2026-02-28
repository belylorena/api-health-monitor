import requests
import time
import yaml


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


def check_api(api):
    print(f"\nChecking API: {api['name']}")
    print(f"URL: {api['url']}")

    start_time = time.time()

    try:
        response = requests.get(api["url"])
        response_time = time.time() - start_time

        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")

        if response.status_code == 200:
            print("Status: OK ✅")
        else:
            print("Status: Unexpected response ⚠️")

        if response_time > api["max_response_time"]:
            print("Performance: Slow response ❌")
        else:
            print("Performance: Within acceptable limit 🚀")

    except requests.exceptions.RequestException as e:
        print("API request failed ❌")
        print(str(e))


if __name__ == "__main__":
    config = load_config()
    for api in config["apis"]:
        check_api(api)