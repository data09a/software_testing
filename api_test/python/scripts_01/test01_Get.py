"""Get request practice
   Case: http://www.google.com
   Request:
        1. Method: GET
   Response:
        2. Response: .url
                     .status_code
                     .text


"""
# 1. import
import requests

# 2.  get url
url = "http://www.msn.com"
r = requests.get(url)

# 3. fetch
print("request url:", r.url)

print("status code：", r.status_code)

print("text content：", r.text)