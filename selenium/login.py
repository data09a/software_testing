from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()

driver.implicitly_wait(10)


url = r"file:///Users/annie/Desktop/registerA.html"

driver.get(url)

driver.find_element_by_css_selector("#userA").send_keys("admin")
sleep(2)

driver.find_element_by_css_selector("#passwordA").send_keys("123456")
sleep(2)

driver.find_element_by_css_selector(".telA").send_keys("123123123")
sleep(2)


driver.find_element_by_css_selector("#emailA").send_keys("abc123@gmail.com")
sleep(2)


driver.find_element_by_css_selector(".telA").clear()
sleep(2)

driver.find_element_by_css_selector(".telA").send_keys("223223223")
sleep(2)

driver.find_element_by_css_selector("button").click()
sleep(2)

driver.quit()