from selenium.webdriver.common.by import By

"""Below is login page elements info"""
#login link
login_link = By.PARTIAL_LINK_TEXT, "Login"
# username
login_username = By.ID, "username"
# password
login_pwd = By.ID, "password"
# verification code
login_verify_code = By.ID, "verify_code"
# login button
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# get error info
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
# click button
login_err_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"

