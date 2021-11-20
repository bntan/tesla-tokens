import os
import base64
import hashlib
import requests
import webbrowser

# Generate parameters

code_verifier = base64.urlsafe_b64encode(os.urandom(86)).rstrip(b"=")
code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier).digest()).rstrip(b"=").decode("utf-8")
state = base64.urlsafe_b64encode(os.urandom(16)).rstrip(b"=").decode("utf-8")

headers = {
    "User-Agent": "",
    "x-tesla-user-agent": "",
    "X-Requested-With": "com.teslamotors.tesla",
}

# Open a session

session = requests.Session()

# GET https://auth.tesla.com/oauth2/v3/authorize

print("***** Open the link below in a browser and authenticate with your TESLA credentials as always *****")
print("")
print("https://auth.tesla.com/oauth2/v3/authorize?audience=https%3A%2F%2Fownership.tesla.com%2F&client_id=ownerapi&code_challenge=" + str(code_challenge) + "&code_challenge_method=S256&locale=en-US&prompt=login&redirect_uri=https%3A%2F%2Fauth.tesla.com%2Fvoid%2Fcallback&response_type=code&scope=openid+email+offline_access&state=" + str(state))
webbrowser.open("https://auth.tesla.com/oauth2/v3/authorize?audience=https%3A%2F%2Fownership.tesla.com%2F&client_id=ownerapi&code_challenge=" + str(code_challenge) + "&code_challenge_method=S256&locale=en-US&prompt=login&redirect_uri=https%3A%2F%2Fauth.tesla.com%2Fvoid%2Fcallback&response_type=code&scope=openid+email+offline_access&state=" + str(state))

print("")
print("***** Once authenticated, you are redirected to an URL which looks like https://auth.tesla.com/void/callback?code={code}&state={state}&issuer={issuer} *****")

print("")
print("***** Grab the {code} in the URL and paste it below  *****")
code = input("Code: ")

# POST https://auth.tesla.com/oauth2/v3/token

data = {
    "grant_type": "authorization_code",
    "client_id": "ownerapi",
    "code_verifier": code_verifier.decode("utf-8"),
    "code": code,
    "redirect_uri": "https://auth.tesla.com/void/callback",
}

response = session.post("https://auth.tesla.com/oauth2/v3/token", headers=headers, json=data)
response.raise_for_status()

print("")
print("***** Your access_token is *****")
print("")
access_token = response.json()["access_token"]
print(access_token)
print("")
print("***** Your refresh_token is *****")
print("")
refresh_token = response.json()["refresh_token"]
print(refresh_token)
