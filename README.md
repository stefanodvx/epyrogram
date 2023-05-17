## EPyrogram: extend the functionality of Pyrogram by enhancing it with new features.
### Installation ⚙️
```bash
pip install git+https://github.com/stefanodvx/epyrogram@main
```

### Example Code ❓
All you need to do is just import epyrogram custom Client and use it like a regular pyrogram Client!
```python3
from epyrogram import Client
from pyrogram import filters

client = Client("bot", api_id=123, api_hash="abc", ...)
client.start()

async def main():
    user_id, chat_id = 123, 456
    await client.send_message(chat_id, f"{user_id}, send your prompt!")
    prompt_message = client.listen_message(
        chat_id=chat_id,
        filters=filters.user(user_id)
    )
    await client.send_message(chat_id, f"{user_id}, your prompt is: {prompt_message.text}")

client.stop()
```