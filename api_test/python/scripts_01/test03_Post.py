import requests

url = "http://127.0.0.1:8000/api/departments/"

# request header
headers = {"Content-Type": "application/json"}

# request json
data = {
        "data": [{
                    "dep_id": "TT702",
                    "dep_name": "TestCollege",
                    "master_name": "Test-Master",
                    "slogan": "Here is Slogan"
                }]
        }

r = requests.post(url, json=data, headers=headers)


print(r.json())


print(r.status_code)

