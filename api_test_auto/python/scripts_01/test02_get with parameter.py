"""
    Method：Get
    Case：
        1. http://www.google.com?id=1001
        2. http://www.google.com?id=1001,1002
        3. http://www.google.com?id=1001&kw=NYC

"""


import requests


url = "http://www.msn.com"


# # case 1
# params = {"id": 1001}


# # case 2
# params = {"id": "1001,1002"}

# # case 3
params = {"id": 1001, "kw": "NYC"}
r = requests.get(url, params=params)

print("Request url:", r.url)

print("Status code：", r.status_code)

print("Text response：", r.text)
