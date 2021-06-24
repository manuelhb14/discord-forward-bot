from copy import Error
import setup
import time
import message
import send_telegram

driver = setup.login()
setup.select_group(6, driver)
# setup.select_channel(2, driver)
setup.select_channel(1, driver)

last_message = message.get_message(driver)

while True:
    try:
        time.sleep(3)
        new_message = message.get_message(driver)
        if new_message != last_message:
            txt, img = message.get_image_text(driver, new_message)
            print(send_telegram.telegram_bot_sendtext("{}\n{}".format(txt, img)))
            last_message = new_message
    except Exception as e:
        txt = message.get_text(new_message)
        print(send_telegram.telegram_bot_sendtext("{}".format(txt)))
        last_message = new_message