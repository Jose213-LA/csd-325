import requests

response = requests.get('http://api.open-notify.org/astros.json')

if response.status_code == 200:
    data = response.json()
    print(f"Number of astronauts in space: {data['number']}")
    print("Names of astronauts:")
    for person in data['people']:
        print(f"- {person['name']} (Craft: {person['craft']})")
else:
    print("Failed to retrieve data.")

