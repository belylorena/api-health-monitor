import yaml
import json
import os
from datetime import datetime
from core.monitor import check_api


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


def save_report(data):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/report_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"\nReport saved to {filename}")


if __name__ == "__main__":
    config = load_config()

    total = 0
    healthy = 0
    slow = 0
    failed = 0

    for api in config["apis"]:
        total += 1
        result = check_api(api)

        if result["healthy"]:
            healthy += 1
        if result["slow"]:
            slow += 1
        if result["failed"]:
            failed += 1

    summary = {
        "total": total,
        "healthy": healthy,
        "slow": slow,
        "failed": failed,
        "timestamp": datetime.now().isoformat()
    }

    print("\n===== EXECUTION SUMMARY =====")
    print(f"Total APIs: {total}")
    print(f"Healthy: {healthy}")
    print(f"Slow: {slow}")
    print(f"Failed: {failed}")

    save_report(summary)