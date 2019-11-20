"""newskylabs/tools/scissors/utils/logger.py:

Initializing the logger.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2019 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2019/11/20"

from kivy.logger import Logger, LOG_LEVELS

## =========================================================
## Initializing Kivy's logger
## ---------------------------------------------------------

def init_logger(logger):
    """Setting up the Kivy logger.
    """

    # Set log level
    log_level = 'debug'
    log_level_code = LOG_LEVELS.get(log_level.lower())
    logger.setLevel(log_level_code)

    # DEBUG
    logger.info('Setting up Scissors Logger: Hello Logger :)')

## =========================================================
## =========================================================

## fin.
