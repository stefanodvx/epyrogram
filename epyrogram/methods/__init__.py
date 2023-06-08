from .listen_message import ListenMessage
from .listen_callback_query import ListenCallbackQuery
from .send_screenshot_notification import SendScreenshotNotification

class Methods(
    ListenMessage,
    ListenCallbackQuery,
    SendScreenshotNotification
):
    pass