#!/bin/env python3
from quoter import replaceWords
import botogram
bot = botogram.create("your api key here")
bot.owner = "KeiTachikawa on telegram, aeres99[at]gmail.com"
bot.after_help = [
   "This bot simply gives new random quotes.",
]


@bot.command("hello")
def hello_command(chat,message, args):
    """This basically says hello, and tells about the bot. Its goal and purpose"""
    chat.send("Hello, I am linux quotes bot. Please note none of these quotes are real, they are made for fun and no cute animals were harmed in its creation")

@bot.command("new")
def new_command(chat,message, args):
    """Send in the new random quote!"""
    output_quote = replaceWords()
    print("*"*10)
    print(output_quote)
    chat.send(output_quote)



if __name__ == "__main__":
    bot.run()

