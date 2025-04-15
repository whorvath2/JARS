from co.deability.jars.error import CustomStatusCode
from co.deability.jars.error.jars_error import JarsError


class RProcessingError(JarsError):
    def __init__(self, message: str) -> None:
        super().__init__(
            message=message, error_code=CustomStatusCode.R_PROCESSING_ERROR.value
        )
