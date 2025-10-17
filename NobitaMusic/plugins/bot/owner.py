from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NobitaMusic import app
from config import BOT_USERNAME
from NobitaMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - 𝚴 𝐎 𝐁 𝚰 𝐓 𝚲
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - 𝚴 𝐎 𝐁 𝚰 𝐓 𝚲
│├─────────────────╯
├┼─────────────────⦿
├┤~ @NOBITA_MUSIC_ROBOT
├┤~ @NOB1TA_SUPPORT
├┤~ @OG_DEFAULTERS_2016
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @ll_NOBITA_DEFAULTERS_ll
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝚴 𝐎 𝐁 𝚰 𝐓 𝚲 ", url=f"https://t.me/ll_NOBITA_DEFAULTERS_ll")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/+ClpXmI00B7UxYjc1"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/NOB1TA_SUPPORT"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/NOB1TA_SUPPORT"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/NOBITA_MUSIC_ROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/tcz7s6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
