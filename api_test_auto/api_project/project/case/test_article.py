import unittest
from api.api_article import ApiArticle
from parameterized import parameterized

# get data
from tools.read_json import ReadJson


# get bookmarked article data
def get_data_add():
    data = ReadJson("article_add.json").read_json()
    # create new empty array, and add json data
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs


# get canceled bookmark data:
def get_data_cancel():
    data = ReadJson("article_cancel.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code")))
    return arrs


# create new test class
class TestArticle(unittest.TestCase):
    # create new bookmark method
    @parameterized.expand(get_data_add())
    def test01_collection(self, url, headers, data, expect_result, status_code):
        r = ApiArticle().api_post_collection(url, headers, data)

        print("Bookmark responded data: ", r.json())

        self.assertEquals(status_code, r.status_code)

        self.assertEquals(expect_result, r.json()["message"])

    # create canceled bookmark method
    @parameterized.expand(get_data_cancel())
    def test02_cancel(self, url, headers, status_code):
        r = ApiArticle().api_delete_article(url, headers)

        print(r.status_code)

        self.assertEquals(status_code, r.status_code)


if __name__ == '__main__':
    unittest.main()