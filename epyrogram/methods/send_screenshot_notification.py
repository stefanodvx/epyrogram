from pyrogram.raw.types import Updates
from pyrogram.raw.functions import messages

from typing import Optional, Union

import epyrogram

class SendScreenshotNotification:
    async def send_screenshot_notification(
        self: "epyrogram.Client",
        chat_id: Union[int, str],
        reply_to_message_id: Optional[Union[int, str]] = None
    ) -> "Updates":
        
        return await self.invoke(
            messages.SendScreenshotNotification(
                peer=await self.resolve_peer(chat_id),
                reply_to_msg_id=reply_to_message_id or 0,
                random_id=self.rnd_id()
            )
        )