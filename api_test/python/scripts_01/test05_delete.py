
import requests

url = "http://127.0.0.1:8000/api/departments/TT702/"
r = requests.delete(url)


print(r.status_code)

