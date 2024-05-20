import requests

# Read the content of the file into a variable
with open(".client_id", "r") as file:
    CLIENT_ID = file.read().strip()

with open(".client_secret", "r") as file:
    CLIENT_SECRET = file.read().strip()

def get_token(refresh_token):
    # make our request using a different grant type and our refresh token
    response = requests.post('https://exist.io/oauth2/access_token', {
        'grant_type':'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    # parse the response into json
    data = response.json()
    print("\nNEW TOKENS")
    print('Access token: ', data['access_token'])
    print('Refresh token:', data['refresh_token'])


if __name__ == "__main__":
    refresh_token = input("Refresh token: ")
    get_token(refresh_token)
