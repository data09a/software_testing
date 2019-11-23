
# class name
class ApiLogin(object):

    # initial the function
    def __init__(self):

        self.url_verify = "http://192.168.176.128/index.php?m=Home&c=User&a=verify"


        self.url_login = "http://192.168.176.128/index.php?m=Home&c=User&a=do_login"

    # request for verify code
    def api_get_verify(self, session):

        session.get(self.url_verify)

    # request to login
    def api_post_login(self, session, username, password, verify_code):

        data = {"username": username,
                "password": password,
                "verify_code": verify_code}

        # return
        return session.post(self.url_login, data=data)