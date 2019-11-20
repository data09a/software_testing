from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()

url = r"file:///Users/annie/Desktop/test_page/registration.html"
driver.get(url)
sleep(3)

current_handle = driver.current_window_handle
print("Current Handle：", current_handle)
sleep(3)

driver.find_element_by_partial_link_text("Register A").click()

sleep(3)

handles = driver.window_handles
print("All Window Handles：", handles)

for h in handles:
    if h != current_handle:

        driver.switch_to.window(h)
        sleep(3)


        driver.find_element_by_css_selector("#userA").send_keys("admin")
        sleep(3)

        driver.find_element_by_css_selector("#passwordA").send_keys("admin")
        sleep(3)

        driver.find_element_by_css_selector(".telA").send_keys("123123123")
        sleep(3)

        driver.find_element_by_css_selector("#emailA").send_keys("abc@gmail.com")


sleep(2)

driver.quit()