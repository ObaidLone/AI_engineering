import requests

response = requests.get("https://httpbin.org/get", params={"q":"test"},timeout=10)
response.raise_for_status()
data=response.json()
print(data["args"])