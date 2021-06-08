from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import keys

driver = webdriver.Firefox(executable_path="./geckodriver.exe")
driver.get("http://www.discord.com/login")
email_input = driver.find_element_by_name("email")
email_input.send_keys(keys.email)
password_input = driver.find_element_by_name("password")
password_input.send_keys(keys.password)
login_button = driver.find_element_by_css_selector("button.marginBottom8-AtZOdT")
login_button.click()
group = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[1]/div[2]/div/div/*[local-name() = 'svg']/*[local-name() = 'foreignObject']/div"))) #TODO: Select where group is located (or by name) div[1] is the variable that changes
time.sleep(1)
group.click()
channel = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/nav/div[3]/div/div[4]/div/div/a") #TODO: Select where channel is located (or by name) div[4] is the variable that changes, starts in 3
time.sleep(2)
channel.click()

last_message = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div/div/div/div/div[position()=last()-1]")
print(last_message.text)

while True:
    try:
        time.sleep(3)
        new_message = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div/div/div/div/div[position()=last()-1]")
        if new_message != last_message:
            print(new_message.text)
            last_message = new_message
    except KeyboardInterrupt:
        print("Logging out")