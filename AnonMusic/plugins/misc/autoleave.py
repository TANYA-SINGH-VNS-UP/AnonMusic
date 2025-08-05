import asyncio
from datetime import datetime

import config
from AnonMusic import app
from AnonMusic.core.call import Anony, autoend
from AnonMusic.utils.database import get_client, is_active_chat, is_autoend
from pyrogram.enums import ChatType

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
                            if i.chat.id not in [config.LOGGER_ID, -1002500829755, -1002204995394]:
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


# Auto End Stream Remove 
