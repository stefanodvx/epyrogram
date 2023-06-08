from pyrogram.raw.types import Config
from pyrogram.raw.functions import help

import epyrogram

class GetConfig:
    async def get_config(
        self: "epyrogram.Client",
    ) -> "Config":
        return await self.invoke(help.GetConfig())