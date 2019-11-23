"""
    Goal：use session object to login and look for my order

    Case data：
        1.verification code：http://192.168.176.128/index.php?m=Home&c=User&a=verify
        2.login：http://192.168.176.128/index.php?m=Home&c=User&a=do_login
        3.order：http://192.168.176.128/index.php/Home/Order/order_list.html
        4.login data
            data = {"username": "ab123",
                    "password": "12345678",
                    "verify_code": 8888}

"""


# 1. import
import requests

# 2. create session object
session = requests.session()

# 3. request and get verify
url_verify = "http://192.168.176.128/index.php?m=Home&c=User&a=verify"
session.get(url_verify)

# 4. request to login
url_login = "http://192.168.176.128/index.php?m=Home&c=User&a=do_login"
data = {"username": "ab123",
        "password": "12345678",
        "verify_code": 8888}
r = session.post(url=url_login, data=data)
# verify if login successfully
print(r.json())

# 5. look for my order
url_order = "http://192.168.176.128/index.php/Home/Order/order_list.html"
r = session.get(url_order)
# print order information
print(r.text)