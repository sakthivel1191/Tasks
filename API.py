import requests

response=requests.get("https://jsonplaceholder.typicode.com/users")
print("Status code:",response.status_code)
users=response.json()
for user in users:
    print("Name:",user["name"])