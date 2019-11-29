import time

from appium import webdriver

desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'

desired_caps = dict()
# mobile phone
desired_caps['platformName'] = 'Android'
# app
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# get driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

driver.start_activity("com.android.mms", ".ui.ConversationList")

time.sleep(5)
driver.quit()

# # install app
# if driver.is_app_installed(" "):
#
#     driver.remove_app("")
# else:
#     driver.install_app("/Users/Desktop/.apk")
