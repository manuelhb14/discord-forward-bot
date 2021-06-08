from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="./geckodriver.exe")
driver.get("http://www.discord.com/login")

time.sleep(5)
driver.close()