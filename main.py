import discord
import os
import requests
import json
import random

#Public Variables
client = discord.Client()

class CommandsMethods:
    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")

        json_data = json.loads(response.text)

        quote_text = json_data[0]['q']
        quote_author = json_data[0]['a']

        final_quote = quote_text + " ~" + quote_author

        return final_quote

    def get_meme(self):
        pass

class FilesMethod:
    def read_from(filename):
        file = open(filename, "r")

        sad_list = file.readlines()
        sad_list = sad_list.split(",")

        file.close()

        return sad_list

    def append_to(filename, message):
        file = open(filename, "a")

        file.write(message)

        file.close()


class BotMethods:
    global client

    @client.event
    async def on_ready():
        print('Logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
        
        elif message.content.startswith('$inspire'):
            Encourage_Method = CommandsMethods()
            quote = Encourage_Method.get_quote()

            await message.channel.send(quote)
            

def main():
    client.run(os.getenv('TOKEN'))

if __name__ == "__main__":
    main()
