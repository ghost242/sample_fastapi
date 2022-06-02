import logging

import uvicorn


logging.getLogger().setLevel(logging.DEBUG)

logging.debug("Set debugging")

def start():
    from src.app import service_initializer

    """Launched with `poetry run start` at root level"""
    service_initializer()

    uvicorn.run("src:service_app", host="0.0.0.0", port=8000, reload=True, )
