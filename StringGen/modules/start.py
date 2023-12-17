from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("astart") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"n",
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)

@Anony.on_message(filters.command("genstring") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"Hai {message.from_user.first_name},\n\nSilahkan Klik Tombol Di Bawah Untuk Mengambil String Session Anda",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
