import os
import sys
import json
import requests

#1) function to get response code, response headers, and data
def get_url(url,timeout):
    try:
        r = requests.get(url,timeout=timeout,allow_redirects=False)
    except requests.exceptions.RequestException as e:
        print (e)
        sys.exit(1)
    status_code = r.status_code
    resp_headers = r.headers
    data = r.json()
    return (status_code,dict(resp_headers),data)

#2) make the request
url = 'https://api.coinmarketcap.com/v1/ticker/ripple/'
timeout = 5
status_code,resp_headers,data = get_url(url,int(timeout))
print(status_code)
print(json.dumps(resp_headers,indent=4,sort_keys=False))

#3) list values of each crypto
for crypto in data:
    print(crypto['price_usd'])



