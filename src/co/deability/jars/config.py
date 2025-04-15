import logging
import os
import sys
from typing import Final

from co.deability.jars.error.environment_error import EnvironmentError

DEBUG: Final[bool] = __debug__ and os.environ.get("FLASK_DEBUG") != "True"

ROOT_LOG_LEVEL: Final[str] = os.environ.get("ROOT_LOG_LEVEL")
APP_LOG_LEVEL: Final[str] = os.environ.get("JARS_LOG_LEVEL")
if not ROOT_LOG_LEVEL or not APP_LOG_LEVEL:
    raise EnvironmentError(
        explanation="Either or both of the environment variables ROOT_LOG_LEVEL and "
        "JARS_LOG_LEVEL are not set."
    )

LOG = logging.getLogger("jars_log")
try:
    logging.getLogger().setLevel(level=ROOT_LOG_LEVEL)
    LOG.setLevel(level=APP_LOG_LEVEL)
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

except ValueError:
    raise EnvironmentError(
        explanation="Either or both of the environment variables ROOT_LOG_LEVEL and "
        "JARS_LOG_LEVEL are set to an unsupported value; use only CRITICAL, FATAL, "
        "ERROR, WARN, WARNING, INFO, or DEBUG."
    )
