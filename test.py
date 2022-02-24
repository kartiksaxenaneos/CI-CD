import requests
api = requests.get("https://gorest.co.in/public/v1/users")
print(f"Response: {api.status_code}")
print(api.json())

