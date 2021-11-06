

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from DTSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DTSongBot import DTbot as app
from DTSongBot import LOGGER

pm_start_text = """
🙆‍♀️ Hey [{}](tg://user?id={}),\n🌷 I'm 🎧 Song Downloader bot  🎵
🙋‍♂️ Made by Programming Boy Corporation ©️\n<b>
🥰 My commands 👇</b>
🍀/song : Download songs via Youtube
🙋‍♂️/about : About Bot
☘️ 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 @HASINDU_HIMASARA\n\n
✍️ මේ BOT ගෙන් පුළුවන් ඕනෙම සින්දුවක් Search කරලා Download කරන්න. 😜\n🙃 ඔයාට සින්දුවක් Download කරන්න ඕන නම් මේ විදිහට Type කරලා Send කරන්න. /song <b>!song name!</b>\n\n☘ Ex:- /song Lily\n<b>🙋‍♂️ Owner: HASINDU</b>\n<b>🙋‍♂️ Admin: Janiru</b>\n🍀 Stay Safe & Good Luck 🍀
◇───────────────◇\n\n✌ Programming Boy Corporation ©️\n\n◇───────────────◇
"""

help_text = """
My commands👇
- /song <song name>: 👀 Download songs via Youtube 👀
-/about : ✌ About Bot ✌
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
