# Discord bot to forward messages from Discord Channel to Telegram Channel

## Using [selenium](https://selenium-python.readthedocs.io/installation.html) library

This project will send all new messages from a channel to a Telegram Channel/Bot/Group/Chat without using Discord bots so you don't have to be an administrator of the Discord group you want to forward the message from.

If you are the administrator of the group we will be creating a Discord bot for this task (Q3 2021).

### Step 1

Install [geckodriver](https://github.com/mozilla/geckodriver/releases) on this directory.

## Step 2.1

Create keys.py file and add your Discord name and password to it.
Example:

```python
email = "one@mail.com"
password = "12345abcde"
```

## Step 2.2

Add your Telegram bot token and chat ID.
Example:

```python
bot_token = '1605383709:AAEIMNG5nQJooD45POSaHbenjUIfFJjbGdw'
bot_chatID = '1444715064' #Test
```

## Step 3

Select the group and channel where you want messages to be forwarded on setup.py. TODO: Select group and channel with the name of it.

## Step 4

Run main.py and a Firefox web browser shouls open with Discord accessing the group and channel you selected. Messages will arrive to the Telegram channel you selected.
