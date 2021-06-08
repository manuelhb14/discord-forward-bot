from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keys

driver = webdriver.Firefox(executable_path="./geckodriver.exe")
driver.get("http://www.discord.com/login")
element = driver.find_element_by_name("email")
element.send_keys(keys.email)
element = driver.find_element_by_name("password")
element.send_keys(keys.password)
time.sleep(5)
driver.close()