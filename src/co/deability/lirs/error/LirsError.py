import logging
from logging import Logger
from typing import Final

LOG: Final[Logger] = logging.getLogger()


class LirsError(Exception):
    """
    Base class for LIRS-specific exceptions.
    """

    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        LOG.error(
            msg=f"{message} (Error code: {error_code})",
            exc_info=self,
            stack_info=__debug__,
        )
