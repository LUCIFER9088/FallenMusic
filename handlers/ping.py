import os
import time
from datetime import datetime

import psutil
from pyrogram import Client, filters
from pyrogram.types import Message

from . import app, boottime
from helpers.ping import get_readable_time
"""


async def bot_sys_stats():
    bot_uptime = int(time.time() - boottime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f"""
ᴜᴘᴛɪᴍᴇ: {get_readable_time((bot_uptime))}
ᴄᴘᴜ: {cpu}%
ʀᴀᴍ: {mem}%
ᴅɪsᴋ: {disk}%"""
    return stats


@app.on_message(filters.command(["ping", f"ping@fallen_music_bot"]))
async def ping(_, message):
    start = datetime.now()
    response = await message.reply_photo(
        photo= "https://telegra.ph/file/f6f020ef5aeeb079b15b9.jpg",
        caption="» ᴘɪɴɢɪɴɢ ʙᴀʙʏ...",
    )
    uptime = await bot_sys_stats()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(
        f"**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ!**\n`⚡{resp} ms`\n\n<b><u>⛧𓆩🖤 𝗙𝝙𝗟𝗟𝝣𝗡 𝗠𝗨𝗦𝗜𝗖 🖤𓆪⛧ sʏsᴛᴇᴍ sᴛᴀᴛs:</u></b>{uptime}"
    )
