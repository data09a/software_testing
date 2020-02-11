from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()

# driver = webdriver.Chrome()

# driver = webdriver.Ie()

driver.get('http://www.google.com')

sleep (3)

driver.quit()