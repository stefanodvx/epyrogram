from typing import Optional, Union
from uuid import uuid4

import epyrogram
import pyrogram
import asyncio

class ListenMessage:
    async def listen_message(
        self: "epyrogram.Client",
        chat_id: Union[int, str],
        timeout: int = 120,
        filters: "pyrogram.filters.Filter" = None,
        uuid: str = None
    ) -> Optional["pyrogram.types.Message"]:
        if not uuid:
            uuid = uuid4().hex
        future = asyncio.get_running_loop().create_future()
        self._listeners[uuid] = {
            "filters": filters & pyrogram.filters.chat(chat_id),
            "future": future,
            "type": pyrogram.types.Message
        }
        future.add_done_callback(lambda _: self._listeners.pop(uuid, None))
        await asyncio.wait_for(future, timeout=timeout)
        try:
            message = await future
            return message
        except asyncio.TimeoutError:
            future.cancel()
            raise