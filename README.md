# API Health Monitor

A configurable CLI tool to monitor API health, response time and performance thresholds.

## Features

- Multiple API monitoring
- Response time validation
- Status code validation
- YAML configuration support
- Error handling

## Configuration

Edit the file:

config/config.yaml

Example:

apis:
  - name: Example API
    url: https://example.com
    max_response_time: 1.0

## How to Run

```bash
pip install -r requirements.txt
python main.py