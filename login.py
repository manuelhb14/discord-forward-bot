from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import keys

driver = webdriver.Firefox(executable_path="./geckodriver.exe")
driver.get("http://www.discord.com/login")
element = driver.find_element_by_name("email")
element.send_keys(keys.email)
element = driver.find_element_by_name("password")
element.send_keys(keys.password)
element = driver.find_element_by_css_selector("button.marginBottom8-AtZOdT")
element.click()
time.sleep(10) #TODO: See if page is loaded
element = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[1]/div[2]/div/div/*[local-name() = 'svg']/*[local-name() = 'foreignObject']/div") #TODO: Select where group is located (or by name) div[1] is the variable that changes
element.click()
element = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[3]/div/div[4]/div/div/a") #TODO: Select where channel is located (or by name) div[4] is the variable that changes, starts in 3
time.sleep(2)
element.click()

element = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div/div/div/div/div[position()=last()-1]")
print(element.get_attribute("innerHTML"))

print(element.text)