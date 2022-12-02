# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0


from telethon.tl.alltlobjects import LAYER
import sys
import os

__author__ = "New-Dev0"
__version__ = "0.2"

LATEST_LAYER = 149
LATEST_TELETHON = "https://github.com/Telethon-Fork/Telethon/archive/refs/heads/main.zip"

if LAYER < LATEST_LAYER:
    sys.stderr.write(
        """
=========================================
Your telegram API LAYER ({}) is outdated.
Consider updating it to ({}) using
'{} -m pip install --no-cache-dir {}'
=========================================
""".format(LAYER, LATEST_LAYER, sys.executable, LATEST_TELETHON),
    )


def update_telethon():
    os.execl(
        sys.executable,
        sys.executable,
        "-m",
        "pip",
        "install",
        "--no-cache-dir",
        LATEST_TELETHON,
    )


def apply():
    from . import methods, custom, events
    from telethon import TelegramClient

    # Rename long name methods..
    TelegramClient.read = TelegramClient.send_read_acknowledge
