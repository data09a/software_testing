from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

# get url , method 1
url = r"file:///Users/annie/Desktop/test_page/registerA.html"

# method 2
# url = r"E:\test_page\registerA.html"

# method 3
# url = r"E:\\test_page\\registerA.html"

driver.get(url)

username = driver.find_element_by_id()


