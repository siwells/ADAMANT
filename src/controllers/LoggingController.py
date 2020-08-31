import logging
import logging.config
import os

from helpers.Constants import *


class LoggingController:
    # create logger
    CONFIG_PATH = os.path.join(BASE_DIR, 'config/logging.conf')
    print(CONFIG_PATH)
    logging.config.fileConfig(CONFIG_PATH)
    logger = logging.getLogger('adamantium')
