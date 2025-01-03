from typing import TYPE_CHECKING
from cardinal import Cardinal

if TYPE_CHECKING:
    from cardinal import Cardinal

from FunPayAPI.updater.events import *
from FunPayAPI.common.enums import *
import logging
from locales.localizer import Localizer
import threading

logger = logging.getLogger("FPC.handlers")
localizer = Localizer()
_ = localizer.translate

LOGGER_PREFIX = "ChatMailing Plugin"
logger.info(f"$MAGENTA{LOGGER_PREFIX} уcпешно запущен.$RESET")

NAME = "ChatMailing"
VERSION = "0.0.1"
DESCRIPTION = "Плагин для флуда сообщениями в чаты"
CREDITS = "@klaymov"
UUID = "7671d8cd-a902-42fb-b867-2c7560610435"
SETTINGS_PAGE = False

CHAT_IDS = ['flood', 'game-41', 'game-2', 'game-3', 'game-4', 'game-123'] # чаты типо
SEND_TIME = 1800 # время в секундах - 30 минут
MESSAGE = """Привет!
"""

def init(cardinal: Cardinal):
    threading.Thread(target=main, args=[cardinal]).start()

def main(c: Cardinal):
    try:
        while True:
            for chat_id in CHAT_IDS:
                c.send_message(chat_id=chat_id, message_text=MESSAGE)
            
            time.sleep(SEND_TIME)
    except Exception as ex:
        logger.error(ex)


BIND_TO_POST_INIT = [init]
BIND_TO_DELETE = None