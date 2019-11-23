import requests


url = "http://www.amazon.com"
r = requests.get(url)

print(r.encoding)


r.encoding = "utf-8"


print(r.text)

print(r.headers)


