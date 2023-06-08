from .listen_message import ListenMessage
from .listen_callback_query import ListenCallbackQuery
from .send_screenshot_notification import SendScreenshotNotification
from .get_config import GetConfig

class Methods(
    ListenMessage,
    ListenCallbackQuery,
    SendScreenshotNotification,
    GetConfig
):
    pass