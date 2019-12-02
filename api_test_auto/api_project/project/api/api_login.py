## STEP 1
# import requests

# new class for login

# new method for login

    # define headers
    # define data
    # define post

## STEP 2
# import requests
import requests

# new class  for login

class ApiLogin(object):

    # new method: login
    def api_post_login(self):
        # define headers
        headers = {"Content-Type": "application/json"}

        # define data
        data = {"mobile": mobile, "code": code}

        # return post
        return requests.post(url, headers=headers, json=data)
