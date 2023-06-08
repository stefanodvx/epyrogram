from pyrogram.types import Message, CallbackQuery
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from .methods import Methods

from typing import Union

import pyrogram
import asyncio
import logging

log = logging.getLogger(__name__)

class Client(pyrogram.Client, Methods):
    def __init__(self, *args, **kwargs):

        # Init pyrogram Client
        super().__init__(
            *args,
            **kwargs
        )

        self._listeners = {}

        for handler in (MessageHandler, CallbackQueryHandler):
            self.dispatcher.add_handler(handler(self._handlers_listener), -999)

        log.debug("Client patched.")

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
