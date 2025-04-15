from http import HTTPStatus

from co.deability.jars.error.jars_error import JarsError


class RScriptError(JarsError):
    def __init__(self, bad_script: str) -> None:
        super().__init__(
            message=f"The supplied script...\n{bad_script}\n...is uninterpretable by R",
            error_code=HTTPStatus.UNPROCESSABLE_CONTENT,
        )
