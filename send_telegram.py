import requests
import keys
import urllib

def telegram_bot_sendtext(bot_message):
    
    bot_token = keys.bot_token
    bot_chatID = keys.bot_chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + urllib.parse.quote_plus(bot_message)

    response = requests.get(send_text)

    return response.json()