import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()

    for user in users:
        print(
            f"Name: {user['name']} | "
            f"Email: {user['email']} | "
            f"City: {user['address']['city']}"
        )
else:
    print("Failed to fetch data")