import requests




url = "http://127.0.0.1:8000/api/departments/TT702/"

headers = {"Content-Type": "application/json"}


data = {
        "data": [{
                    "dep_id": "TT702",
                    "dep_name": "TestTT702updateCollege",
                    "master_name": "Test-Master",
                    "slogan": "Here is Slogan"
                }]
        }

r = requests.put(url, json=data, headers=headers)


print(r.json())

print(r.status_code)

