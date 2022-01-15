import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f6f020ef5aeeb079b15b9.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━
🖤 ʜᴇʏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs...
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ /
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦 🖤 𝗕𝗢𝗬](https://t.me/anonymous_was_bot)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/anonymous_was_bot) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😫ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ​😫", url="https://t.me/fallen_music_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "😘ᴄʀᴇᴀᴛᴏʀ😘", url="https://t.me/anonymous_was_bot"
                    ),
                    InlineKeyboardButton(
                        "💔sᴜᴘᴘᴏʀᴛ💔", url="https://t.me/DevilsHeavenMF"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🤔sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​🤔", url="https://t.me/DevilsHeavenMF"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f6f020ef5aeeb079b15b9.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💞sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​💞", url=f"https://t.me/DevilsHeavenMF")
                ]
            ]
        ),
    )

@Client.on_message(filters.command("ping") & ~filters.private & ~filters.channel & ~filters.group)
async def gstart(_, message: Message):
      await message.reply_text("""**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !🖤**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💔sᴜᴘᴘᴏʀᴛ💔", url="https://t.me/DevilsHeavenMF")
                ]
            ]
        )
   )
