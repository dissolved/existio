from urllib.parse import urlencode

URL = "https://exist.io/oauth2/authorize"
REDIRECT_URI = "http://localhost:8000/"

# Define the file path
file_path = ".client_id"

# Read the content of the file into a variable
with open(file_path, "r") as file:
    CLIENT_ID = file.read().strip()

# the parameters we'll be sending
params = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": "media_write",
}

# let's encode them appropriately for a URL
querystring = urlencode(params)
# and finally print the complete result to the terminal
print(f"{URL}?{querystring}")
