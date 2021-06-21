from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import keys

def login():
    driver = webdriver.Firefox(executable_path="./geckodriver.exe")
    driver.get("http://www.discord.com/login")
    email_input = driver.find_element_by_name("email")
    email_input.send_keys(keys.email)
    password_input = driver.find_element_by_name("password")
    password_input.send_keys(keys.password)
    login_button = driver.find_element_by_css_selector("button.marginBottom8-AtZOdT")
    login_button.click()
    return driver

def select_group(group, driver):
    group = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[{}]/div[2]/div/div/*[local-name() = 'svg']/*[local-name() = 'foreignObject']/div".format(group))))
    time.sleep(1)
    group.click()

def select_channel(channel, driver):
    # channel = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[{}]/div/div[14]/div/div/a".format(channel+2)) 
    channel = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[4]/div/div[3]/div/div/a".format(channel+2)) 
    time.sleep(2)
    channel.click()

