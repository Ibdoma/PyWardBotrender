import os
from pathlib import Path
import logging
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

# Define the host and port
HOST = '0.0.0.0'
PORT = 4000

# Your existing setup
if not Path(config_dir/"user.session").exists():
    logger.info("Log-in with your phone number")
user.start()

# Your existing bot setup
for dialog in user.get_dialogs():
    pass

Bot().add_admin(user.get_me().id)  # Add user id to admin database
if not Path(config_dir/"bot.session").exists():
    logger.info("Log-in with you bot token")
bot.start()
logger.info("Bot started")
logger.info(f"Bot username: @{bot.get_me().username}")

# Run the server on the specified port
async def handle(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.router.add_get('/', handle)

if __name__ == '__main__':
    web.run_app(app, host=HOST, port=PORT)

idle()
bot.stop()
