## TESLA tokens

This script helps you get your TESLA access_token and refresh_token in order to connect to third party applications (Teslamate, TeslaFi, ABRP...) without providing them your TESLA credentials.
The script does not require your TESLA credentials. It will redirect you to TESLA site to authenticate as always (so only TESLA knowns your credentials). 

## Prerequisites
 
- Python 3

## Download dependencies

`$ pip install -r requirements.txt`

## Execution

- Execute command
`$ python tesla-tokens.py`

```
***** Open the link below in a browser and authenticate with your TESLA credentials as always *****

https://auth.tesla.com/oauth2/v3/authorize?audience=https%3A%2F%2Fownership.tesla.com%2F&client_id=ownerapi&code_challenge=G1Prx9SX7qijLnAkMyIED05uAKUIl_srHHg-ygBUy9s&code_challenge_method=S256&locale=en-US&prompt=login&redirect_uri=https%3A%2F%2Fauth.tesla.com%2Fvoid%2Fcallback&response_type=code&scope=openid+email+offline_access&state=k6Cygr32UEG51Qh5Nlv1wA
```

- Open the provided link in a browser and authenticate with your TESLA credentials as always

![](https://raw.githubusercontent.com/bntan/tesla-tokens/master/resources/tesla_authentication.png)

- Once authenticated, you are redirected to an URL which looks like https://auth.tesla.com/void/callback?code={code}&state={state}&issuer={issuer}

![](https://raw.githubusercontent.com/bntan/tesla-tokens/master/resources/tesla_authorization_code.png)

- Grab the {code} in the URL and paste it on the screen

```
***** Grab the {code} in the URL and paste it below  *****
Code: db5810a1ca22895bca47f534ddddb7797f00eac97375762144b867fe0e10
```

- Your access_token et refresh_token are printed on the screen

```
***** Your access_token is *****

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilg0RmNua0RCUVBUTnBrZTZiMnNuRi04YmdVUSJ9.[...]

***** Your refresh_token is *****

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilg0RmNua0RCUVBUTnBrZTZiMnNuRi04YmdVUSJ9.[...]
```