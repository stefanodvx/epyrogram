## EPyrogram

**EPyrogram** is an extension of the Pyrogram library that enhances its functionality with new features.

## Installation
You can install EPyrogram using **pip**:

```bash
pip install git+https://github.com/stefanodvx/epyrogram@main
```

## Features
EPyrogram provides a **custom Client** class that can be used just like the regular Pyrogram Client. It adds new methods and functionalities while maintaining compatibility with existing Pyrogram code. This means that EPyrogram will always **rely on your original Pyrogram installation** and will always be up-to-date!

## Example Code
```python3
from epyrogram import Client
from pyrogram import filters

import asyncio

client = Client("bot", api_id=123, api_hash="abc", ...)

async def main():
    await client.start()
    user_id, chat_id = 123, 456
    await client.send_message(chat_id, f"{user_id}, send your prompt!")
    prompt_message = await client.listen_message(
        chat_id=chat_id,
        filters=filters.user(user_id)
    )
    await client.send_message(chat_id, f"{user_id}, your prompt is: {prompt_message.text}")
    await client.stop()

asyncio.run(main())
```
*In this example, the EPyrogram Client is used to create a bot client. It starts the client, sends a prompt message to a specific chat, listens for a response from a specific user, and sends another message with the received prompt.*

## Documentation
Work in progress...

## Contributing
Contributions to EPyrogram are welcome! If you have any bug reports, feature requests, or pull requests, please open an issue on the GitHub repository.

## Acknowledgements
EPyrofrap is based on the original Pyrogram library developed by [Dan](https://github.com/delivrance) and its contributors.
