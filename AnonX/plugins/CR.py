import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين فينوم","المطورين","مطورين","مطورين Venom"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/fdc065a855d2c6b59ef96.jpg",
        caption=f"""**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين فينوم ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙀𝙇𝙍𝘼𝙎𝘼𝙈 ‌𝅘𝅥𝅯 ", url=f"https://t.me/Mahmod777777"), 
                 ],[
                    InlineKeyboardButton(
                        "𝗧𝗨𝗥𝗕𝗢 𖤍", url=f"https://t.me/A7A_BGAAD"),   
                ],[
                
                    InlineKeyboardButton(
                        "𝅘𝅥𝅯𝙎𝙊𝙐𝙍𝘾𝙀 𝙑𝙀𝙉𝙊𝙈 𝅘𝅥𝅯", url=f"https://t.me/Ve_m1"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["الرسام","تربو","رسام","مبرمج","RASAM","rasam"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("DEV_TOM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["تربو","تربو","تربو","رسام","Turbo","Turbo"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["رسام","الرسام","رسام","محمود","رسام","رسام"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("dr_criss")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["تربو","تربو","تربو","تربو","تربو"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("C1_I_I")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/fdc065a855d2c6b59ef96.jpg",
        caption=f"""**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس فينوم\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙀𝙇𝙍𝘼𝙎𝘼𝙈 ‌𝅘𝅥𝅯", url=f"https://t.me/Mahmod777777"), 
                 ],[
                
                    InlineKeyboardButton(
                        "𝅘𝅥𝅯𝙎𝙊𝙐𝙍𝘾𝙀 𝙑𝙀𝙉𝙊𝙈 𝅘𝅥𝅯", url=f"https://t.me/Ve_m1"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/fdc065a855d2c6b59ef96.jpg",
        caption=f"""**𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯𝗩𝗘𝗡𝗢𝗠𝅘𝅥𝅯𓏳𓏳𓏳𓏳𝅘𝅥𝅯**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس فينوم\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙀𝙇𝙍𝘼𝙎𝘼𝙈 ‌𝅘𝅥𝅯", url=f"https://t.me/Mahmod777777"), 
                 ],[
                
                    InlineKeyboardButton(
                        "𝅘𝅥𝅯𝙎𝙊𝙐𝙍𝘾𝙀 𝙑𝙀𝙉𝙊𝙈 𝅘𝅥𝅯", url=f"https://t.me/Ve_m1"),
                ],

            ]

        ),

    )



    
