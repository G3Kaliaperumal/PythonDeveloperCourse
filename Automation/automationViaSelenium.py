# Reference Link: https://selenium-python.readthedocs.io/
# Install chromedriver before proceeding. Link is provided in the above mentioned document.
# To test selenium code use the link: https://www.seleniumeasy.com/test/
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
button = chrome_browser.find_element_by_class_name('btn-default')
print(button.get_attribute('innerHTML'))
