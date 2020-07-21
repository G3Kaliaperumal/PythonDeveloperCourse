# Reference Link: https://selenium-python.readthedocs.io/
# Install chromedriver before proceeding. Link is provided in the above mentioned document.
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
