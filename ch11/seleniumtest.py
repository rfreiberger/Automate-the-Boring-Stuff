#! python3

# Before you run this, the following is required
# 1) Python3
# 2) Selenium 
#
# To install Python3, you can download and install Anaconda
#
# To install Selenium
# C:\> pip install selenium

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('my_user_name')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('Password1')
passwordElem.submit()