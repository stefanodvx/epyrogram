from .client import EClient

import pyrogram

def patch(client: pyrogram.Client) -> EClient:

    if not isinstance(client, pyrogram.Client):
        raise TypeError("You did not provide any Pyrogram Client.")

    init_signature = pyrogram.Client.__init__.__annotations__
    client_args = {
        arg: getattr(client, arg)
        for arg in init_signature.keys()
        if arg != "self"
    }
    return EClient(**client_args)