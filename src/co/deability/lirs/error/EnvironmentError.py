import sys
from http import HTTPStatus

from co.deability.lirs.error.LirsError import LirsError


class EnvironmentError(LirsError):
    """
    Thrown when the LIRS API is being run in a malformed environment.
    """

    def __init__(self, explanation: str):
        super().__init__(
            message=f"LIRS cannot start: {explanation}",
            error_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        )
        sys.exit(explanation)
