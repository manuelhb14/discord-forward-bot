def get_message(driver):
    last_message = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div/div/div/div/div[position()=last()-1]")
    return last_message

def get_image_text(driver, message):
    return (message.text, driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div[1]/div/div/div/div[position()=last()-1]/div[2]/div/a/img").get_attribute('src')) # Get (text, image)

def get_text(message):
    return (message.text) # Get (text, image)