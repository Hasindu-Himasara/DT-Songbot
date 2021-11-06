

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from DTSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DTSongBot import DTbot as app
from DTSongBot import LOGGER

pm_start_text = """
🙆‍♀️ Hey [{}](tg://user?id={}),\n🌷 I'm 🎧 Song Downloader bot  🎵
🙋‍♂️ Made by Programming Boy Corporation ©️\n<b>
🥰 My commands👇</b>
🍀/song : Download songs via Youtube
🍀/saavn : Download songs via JioSaavn
🍀/deezer : Download songs via Deezer
🍀/Send Youtube url to my pm for download it on audio format.\n\n
☘️ 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 @HASINDU_HIMASARA\n
🍀 Stay Safe & Good Luck 🍀\n\n
◇───────────────◇\n◇Programming Boy Corporation ©️\n◇───────────────◇
"""

help_text = """
My commands👇
- /song <song name>: download songs via Youtube
- /saavn <song name>: download songs via JioSaavn
- /deezer <song name>: download songs via Deezer
- Send youtube url to my pm for download it on audio format
A bot by @ankivectorUpdates
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🛠 Updates channel 🛠", url="https://t.me/TECH_WIDE_OFFICIAL"
                    ),
                    InlineKeyboardButton(
                        text="🍀 Support Group 🍀", url="https://t.me/TECH_WIDE_GROUP"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("DTSongBot is online.")
idle()
