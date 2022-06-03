import discord
import requests
from datetime import datetime
from config import TOKEN, CHANNEL_ID, MAX_VIEWS


client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != CHANNEL_ID:
        return

    if '!views' in message.content:
        try:
            number_of_views = int(float(message.content.split(' ')[1]))
            link = message.content.split(' ')[2]


            if number_of_views > MAX_VIEWS:
                response = f'You can only have a maxmimum of {MAX_VIEWS} views'
                await message.channel.send(response)
                return

            embed = discord.Embed(
                title='eBay Views Bot',
                description=f'Adding {number_of_views} views...',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='eBay Link', value=f'{link}')
            await message.channel.send(embed=embed)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-GB,en;q=0.9',
                'dnt': '1',
                'referer': 'https://www.ebay.co.uk/',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                'sec-ch-ua-full-version': '"102.0.5005.63"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
            }

            for i in range(number_of_views):
                requests.get(link, headers=headers)

            embed = discord.Embed(
                title='eBay Views Bot',
                description=f'Added {number_of_views} views.',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='eBay Link', value=f'{link}')
            await message.channel.send(embed=embed)
        except:
            response = 'An error occurred with your request.'
            await message.channel.send(response)


client.run(TOKEN)