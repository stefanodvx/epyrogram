from pyrogram.types import Message, CallbackQuery
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from typing import Union
from uuid import uuid4

import pyrogram
import asyncio
import logging

class Client(pyrogram.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logger = logging.getLogger("pyrogram.epyrogram.client")
        self.logger.debug("Client patched.")

        for handler in (MessageHandler, CallbackQueryHandler):
            self.dispatcher.add_handler(handler(self._handlers_listener), -999)

        self._listeners = {}

    async def listen(
        self,
        chat_id: Union[int, str],
        timeout: int = 120,
        filters: pyrogram.filters.Filter = None,
        uuid: str = uuid4().hex
    ):
        future = asyncio.get_running_loop().create_future()
        self._listeners[uuid] = {
            "filters": filters & pyrogram.filters.chat(chat_id),
            "future": future
        }
        future.add_done_callback(lambda _: self._listeners.pop(uuid, None))
        await asyncio.wait_for(future, timeout=timeout)
        return future

    async def _handlers_listener(
        self,
        client: pyrogram.Client,
        update: Union[Message, CallbackQuery]
    ):
        for listener in self._listeners.values():
            if not isinstance(update, listener["type"]):
                continue
            if not await listener["filters"](client, update):
                continue
            future: asyncio.Future = listener["future"]
            future.set_result(update)
            return await update.stop_propagation()
        await update.continue_propagation()