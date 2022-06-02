import logging

from src.app import service_initializer


def pytest_sessionstart():
    logging.getLogger().setLevel(logging.DEBUG)

    logging.debug("test session start")
    service_initializer()