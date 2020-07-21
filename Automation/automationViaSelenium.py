# Reference Link: https://selenium-python.readthedocs.io/
# Install chromedriver before proceeding. Link is provided in the above mentioned document.
# To test selenium code use the link: https://www.seleniumeasy.com/test/
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Hello!!')

show_msg_button = chrome_browser.find_element_by_class_name('btn-default')
show_msg_button.click()

output_msg = chrome_browser.find_element_by_id('display')
assert 'Hello!!' in output_msg.text

chrome_browser.quit()
