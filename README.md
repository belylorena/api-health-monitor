
# 🧪 API Health Monitor

A lightweight API monitoring tool built for QA Engineers.

This tool allows you to monitor multiple APIs, validate response status
codes, check SLA performance thresholds, and automatically generate
structured JSON reports with historical timestamps.

## 🚀 Why This Project?

In real-world QA environments, validating API health and response time
is essential for:

-   SLA compliance
-   Production monitoring
-   Regression validation
-   CI/CD pipeline integration
-   Automated quality gates

This tool simulates a simplified internal monitoring system.

## ✨ Features

-   ✅ Multi-API monitoring via YAML configuration
-   ✅ HTTP status validation
-   ✅ SLA validation (max response time)
-   ✅ Execution summary
-   ✅ Historical JSON report generation
-   ✅ Clean and modular architecture

## 📂 Project Structure

api-health-monitor/ 
│
├── main.py \# Entry point 
├── requirements.txt
├── README.md │ 
├── config/ 
│ └── config.yaml \# API configuration 
│ 
├──core/ 
│ └── monitor.py \# API validation logic 
│ └── reports/ \#Auto-generated execution reports

## ⚙️ Installation

```bash  
git clone <your-repository-url>  
cd api-health-monitor  
  
python -m venv venv  
venv\Scripts\activate  
  
pip install -r requirements.txt  
```

## ▶️ Running the Monitor

```bash 
python main.py
```

Example output:
```bash 
Checking API: JSONPlaceholder Post 1 
Status Code: 200 
Response Time: 0.52 seconds 
Status: OK ✅ 
Performance: Within acceptable limit 🚀

===== EXECUTION SUMMARY ===== 
Total APIs: 2 
Healthy: 2 
Slow: 0 
Failed: 0

Report saved to reports/report_YYYY-MM-DD_HH-MM-SS.json
```

## ⚙️ Configuration

Edit the file:

```bash 
config/config.yaml
```

Example:

```bash 
apis:
  - name: JSONPlaceholder Post 1
    url: https://jsonplaceholder.typicode.com/posts/1
    max_response_time: 0.5

  - name: JSONPlaceholder Users
    url: https://jsonplaceholder.typicode.com/users
    max_response_time: 0.5
```    

## 📊 Generated Report Example

```bash 
{
  "total": 2,
  "healthy": 2,
  "slow": 0,
  "failed": 0,
  "timestamp": "2026-02-28T18:52:31"
}
``` 

## 🧠 Tech Stack

-   Python 3
-   Requests
-   PyYAML

------------------------------------------------------------------------

## 🎯 Future Improvements

-   Email alert integration
-   Slack webhook notifications
-   HTML report generation
-   Docker support
-   CI/CD integration (GitHub Actions)

------------------------------------------------------------------------

## 👩‍💻 Author

Isabelly Lorena\
QA Engineer \| API Testing \| Automation Enthusiast

------------------------------------------------------------------------

⭐ If you find this useful, consider giving it a star!