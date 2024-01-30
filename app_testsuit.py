import requests
import json
import sys
url = "http://127.0.0.1:8000/test_suite/execute_test_suite/"  # Replace 'yourdomain.com' with your actual domain or localhost address


data = {"project_id": 1, "test_suite_id": sys.argv[1]}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())

