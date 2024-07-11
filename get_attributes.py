import requests
from pprint import pprint

# Define the file path
file_path = ".api_token"

# Read the content of the file into a variable
with open(file_path, "r") as file:
    TOKEN = file.read().strip()

url = "https://exist.io/api/2/attributes/with-values/"

# make sure to authenticate ourselves with our token
response = requests.get(url, headers={"Authorization": f"Token {TOKEN}"})

if response.status_code == 200:
    data = response.json()
    # pretty print the json
    pprint(data)
else:
    print("Error!", response.content)
