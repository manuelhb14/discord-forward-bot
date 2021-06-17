def get_message(driver):
    last_message = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/div/div/div/div/div[position()=last()-1]")
    return last_message