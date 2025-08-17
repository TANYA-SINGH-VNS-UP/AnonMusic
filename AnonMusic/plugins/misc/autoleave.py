import asyncio
from datetime import datetime

import config
from AnonMusic import app
from AnonMusic.core.call import Anony, autoend
from AnonMusic.utils.database import get_client, is_active_chat, is_autoend
from pyrogram.enums import ChatType

# AUTO LEAVE ASSISTANTS
async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT:
        while not await asyncio.sleep(config.ASSISTANT_LEAVE_TIME):
            from AnonMusic.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.get_dialogs():
                        if i.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP, ChatType.CHANNEL]:
                            if i.chat.id not in [config.LOGGER_ID, -1001511253627, -1001511253627]:
                                if left == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        left += 1
                                    except:
                                        continue
                except:
                    pass

asyncio.create_task(auto_leave())


# AUTO END INACTIVE STREAMS
async def auto_end():
    if config.AUTO_END_VC_STREAM:
        while not await asyncio.sleep(5):
            ender = await is_autoend()
            if not ender:
                continue
            for chat_id in autoend:
                timer = autoend.get(chat_id)
                if not timer:
                    continue
                if datetime.now() > timer:
                    if not await is_active_chat(chat_id):
                        autoend[chat_id] = {}
                        continue
                    autoend[chat_id] = {}
                    try:
                        await Anony.stop_stream(chat_id)
                    except:
                        continue
                    try:
                        await app.send_message(
                            chat_id,
                            "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
                        )
                    except:
                        continue

asyncio.create_task(auto_end())
