import unittest
from api.api_channels import ApiChannels
from parameterized import parameterized

from tools.read_json import ReadJson


def get_data():
    data = ReadJson("channel.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs


class TestClannels(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_channels(self, url, headers, expect_result, status_code):

        r = ApiChannels().api_get_channels(url, headers)

        print(r.json())

        self.assertEquals(status_code, r.status_code)

        self.assertEquals(expect_result, r.json()['message'])


if __name__ == '__main__':
    unittest.main()