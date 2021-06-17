import startup
import time
import message

driver = startup.login()
startup.select_group(6, driver)
startup.select_channel(2, driver)

last_message = message.get_message(driver)

while True:
    try:
        time.sleep(3)
        new_message = message.get_message(driver)
        if new_message != last_message:
            print(new_message.text)
            last_message = new_message
    except KeyboardInterrupt:
        print("Logging out")