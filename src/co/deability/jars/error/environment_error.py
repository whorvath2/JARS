import sys
from http import HTTPStatus

from co.deability.jars.error.jars_error import JarsError


class EnvironmentError(JarsError):
    """
    Thrown when the JARS API is being run in a malformed environment.
    """

    def __init__(self, explanation: str):
        super().__init__(
            message=f"JARS cannot start: {explanation}",
            error_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        )
        sys.exit(explanation)
