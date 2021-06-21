from copy import Error
import setup
import time
import message

driver = setup.login()
setup.select_group(6, driver)
# setup.select_channel(2, driver)
setup.select_channel(1, driver)

last_message = message.get_message(driver)
message.get_data(driver, last_message)

while True:
    try:
        time.sleep(3)
        new_message = message.get_message(driver)
        if new_message != last_message:
            message.get_data(driver, new_message)
            last_message = new_message
    except Exception as e:
        pass