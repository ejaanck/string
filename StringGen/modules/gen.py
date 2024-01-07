import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from StringGen import Anony
from StringGen.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ᴛᴇʟᴇᴛʜᴏɴ"
    elif old_pyro:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v1"
    else:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v2"

    await message.reply_text(f"» ʟᴀɢɪ ᴄᴏʙᴀ {ty} ɴɢᴀᴍʙɪʟ sᴛʀɪɴɢ ᴀɴᴅᴀ...")

    try:
        api_id = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴍᴀsᴜᴋɪɴ ᴀᴘɪ ɪᴅ ʟᴜ ʙᴜʀᴜ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 𝟻 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Anony.send_message(
            user_id,
            "» ᴀᴘɪ ɪᴅ ʟᴜ sᴀʟᴀʜ ʙʟᴏɢ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴍᴀsᴜᴋɪɴ ᴀᴘɪ ʜᴀsʜ ʟᴜ ʙᴜʀᴜ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 𝟻 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Anony.send_message(
            user_id,
            "» ᴀᴘɪ ʜᴀsʜ ʟᴜ sᴀʟᴀʜ ʙʟᴏɢ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» ᴍᴀsᴜᴋɪɴ ɴᴏᴍᴏʀ ᴛᴇʟᴇ ʟᴜ ʙᴜʀᴜ :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 𝟻 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Anony.send_message(user_id, "» ʟᴀɢɪ ɴʏᴏʙᴀ ɴɢɪʀɪᴍɪɴ ᴏᴛᴘ ᴋᴇ ᴀᴋᴜɴ ʟᴜ...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Anony.send_message(
            user_id,
            f"» ɢᴀɢᴀʟ ɴɢɪʀɪᴍ ᴋᴏᴅᴇ ᴏᴛᴘ ᴋᴇ ᴀᴋᴜɴ ʟᴜ.\n\nʜᴀʀᴀᴘ ᴛᴜɴɢɢᴜ {f.value or f.x} sᴇᴄᴏɴᴅs ᴅᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴀᴘɪ ʜᴀsʜ ᴀᴛᴀᴜ ᴀᴘɪ ɪᴅ ʟᴜ sᴀʟᴀʜ ʙʟᴏɢ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Anony.send_message(
            user_id,
            "» ᴍᴀsᴜᴋɪɴ ɴᴏᴍᴏʀ ᴛᴇʟᴇ sᴀʟᴀʜ ʙʟᴏɢ ʟᴜ\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    try:
        otp = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"ᴍᴀsᴜᴋɪɴ ᴋᴏᴅᴇ ᴏᴛᴘ ʟᴜ ᴅᴀʀɪ ɴᴏᴍᴏʀ {phone_number}.\n\nᴋᴀʟᴏ ᴋᴏᴅᴇ ᴏᴛᴘɴʏᴀ <code>12345</code>, ᴛᴏʟᴏɴɢ ᴋɪʀɪᴍᴋᴀɴ sᴇᴘᴇʀᴛɪ ɪɴɪ <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 10 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Anony.send_message(
            user_id,
            "» <b>ᴋᴏᴅᴇ ᴏᴛᴘ ʏɢ ʟᴜ ᴍᴀsᴜᴋɪɴ sᴀʟᴀʜ.</b>\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Anony.send_message(
            user_id,
            "» <b>ᴋᴏᴅᴇ ᴏᴛᴘ ʏɢ ʟᴜ ᴍᴀsᴜᴋɪɴ ᴇxᴘɪʀᴇᴅ.</b>\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Anony.ask(
                identifier=(message.chat.id, user_id, None),
                text="» ᴍᴀsᴜᴋɪɴ ᴘᴡ ᴠᴇʀɪғ 𝟸 ʟᴀɴɢᴋᴀʜ ʟᴜ :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Anony.send_message(
                user_id,
                "» ʏᴀʜ ᴋᴇʟᴀᴍᴀᴀɴ ᴋᴇʙᴜʀᴜ 𝟻 ᴍᴇɴɪᴛ ᴋᴀɴ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Anony.send_message(
                user_id,
                "» ᴘᴡ ᴠᴇʀɪғ 𝟸 ʟᴀɴɢᴋᴀʜ ʟᴜ sᴀʟᴀʜ.\n\nᴋʟɪᴋ /start ʙᴜᴀᴛ ᴀᴍʙɪʟ sᴛʀɪɴɢ ʙᴀʀᴜ.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Anony.send_message(user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code>")

    try:
        txt = "ɴɪʜ {0} sᴛʀɪɴɢ sᴇssɪᴏɴ ʟᴜ\n\n<code>{1}</code>\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={2}>sɪ ᴧꝛᴧʙ</a>\n☠ <b>ɴᴏᴛᴇ :</b> Jᴀɴɢᴀɴ ʟᴜ sᴇʙᴀʀɪɴ ʙᴜᴀᴛ ᴘɪɴJᴏʟ."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("codekita"))
            await client(JoinChannelRequest("stayheresay"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("jxsupport")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Anony.send_message(
            chat_id=user_id,
            text=f"ɴɪʜ sᴛʀɪɴɢ ʟᴜ ᴜᴅᴀʜ Jᴀᴅɪ {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\nᴄᴇᴋ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ ʟᴜ ʏᴀɴɢ ʙᴀɴʏᴀᴋ ʙᴏᴋᴇᴘɴʏᴀ.\n\nᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ <a href={SUPPORT_CHAT}>sɪ ᴧꝛᴧʙ</a>.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ ʟᴜ",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» ɴɢᴇʙᴀᴛᴀʟɪɴ ᴘʀᴏsᴇs ɴɢᴀᴍʙɪʟ sᴛʀɪɴɢ ʟᴜ.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» sᴜᴋsᴇs ɴɢᴇʀᴇsᴛᴀʀᴛ ʙᴏᴛ.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss.", reply_markup=retry_key
        )
        return True
    else:
        return False
