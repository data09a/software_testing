import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson


def get_data():
    datas = ReadJson("login_more.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expect_result"),
                     data.get("status_code")))
    return arrs


class TestLogin(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_login(self, url, mobile, code, expect_result, status_code):
        s = ApiLogin().api_post_login(url, mobile, code)

        print("查看响应结果：", s.json())

        self.assertEquals(expect_result, s.json()['message'])

        self.assertEquals(status_code, s.status_code)


if __name__ == '__main__':
    unittest.main()
