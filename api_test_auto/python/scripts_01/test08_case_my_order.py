"""
    Goal：Get my order information

    Case data：
        1.verification code：http://192.168.176.128/index.php?m=Home&c=User&a=verify
        2.login：http://192.168.176.128/index.php?m=Home&c=User&a=do_login
        3.order：http://192.168.176.128/index.php/Home/Order/order_list.html
        4.login data
            data = {"username": "ab123",
                    "password": "12345678",
                    "verify_code": 8888}

"""

## Step 1 (get cookies)
import requests


url_verify_code = "http://192.168.176.128/index.php?m=Home&c=User&a=verify"
r = requests.get(url_verify_code)

r_cookie = r.cookies


print("The cookie is：", r_cookie['PHPSESSID'])

cookies = {"PHPSESSID": r_cookie['PHPSESSID']}

## Step 2 (login)
url_login = "http://192.168.176.128/index.php?m=Home&c=User&a=do_login"
data = {"username": "ab123",
        "password": "12345678",
        "verify_code": 8888}
r = requests.post(url=url_login, data=data, cookies=cookies)

# verify if login successfully
print(r.json())

## Step 3 (look for my order)
url_order = "http://192.168.176.128/index.php/Home/Order/order_list.html"
r = requests.get(url=url_order, cookies=cookies)
print(r.text)
