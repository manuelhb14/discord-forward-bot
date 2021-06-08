from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import keys

driver = webdriver.Firefox(executable_path="./geckodriver.exe")
driver.get("http://www.discord.com/login")
element = driver.find_element_by_name("email")
element.send_keys(keys.email)
element = driver.find_element_by_name("password")
element.send_keys(keys.password)
# element = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/form/div/div/div[1]/div[2]/button[2]")
element = driver.find_element_by_css_selector("button.marginBottom8-AtZOdT")
element.click()
time.sleep(5)
driver.close()