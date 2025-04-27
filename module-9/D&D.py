import requests

# API endpoint for the "Blinded" condition
url = "https://www.dnd5eapi.co/api/conditions/blinded"

# Send the GET request
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# If the request is successful, format and print the data
if response.status_code == 200:
    data = response.json()

    print("\nD&D 5e Condition Info")
    print("=========================")
    print(f"Index       : {data['index']}")
    print(f"Name        : {data['name']}")
    print(f"URL         : {data['url']}")
    print(f"Last Updated: {data['updated_at']}\n")

    print("Description:")
    print("------------")
    for line in data['desc']:
        print(line)

else:
    print("Failed to retrieve data from the API.")
