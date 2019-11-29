import pytest
class TestLogin:

    def setup(self):
        print("------->setup_method")
    def teardown(self):
        print("------->teardown_method")
    def test_a(self):
        print("------->test_a")
    def test_b(self):
        print("------->test_b")