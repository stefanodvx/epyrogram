from pyrogram.filters import Filter
from pyrogram.types import CallbackQuery

from typing import Optional
from uuid import uuid4

import epyrogram
import asyncio

class ListenCallbackQuery:
    async def listen_callback_query(
        self: "epyrogram.Client",
        timeout: int = 120,
        filters: "Filter" = None,
        uuid: str = None
    ) -> Optional["CallbackQuery"]:
        if not uuid:
            uuid = uuid4().hex
        future = asyncio.get_running_loop().create_future()
        self._listeners[uuid] = {
            "filters": filters,
            "future": future,
            "type": CallbackQuery
        }
        future.add_done_callback(lambda _: self._listeners.pop(uuid, None))
        await asyncio.wait_for(future, timeout=timeout)
        try:
            message = await future
            return message
        except asyncio.TimeoutError:
            future.cancel()
            raise