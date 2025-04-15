import inspect
from http import HTTPStatus
from typing import Optional, List

from flask import Response, make_response, jsonify
from werkzeug.exceptions import InternalServerError

from co.deability.jars import config
from co.deability.jars.config import LOG
from co.deability.jars.error.jars_error import JarsError


def handle_assertion_errors(assertion_error: AssertionError) -> Response:
    if config.DEBUG:
        stack: List[inspect.FrameInfo] = inspect.stack()
        internal_message: str = (
            f"Assertion error raised in {stack[1].function} after call from "
            f"{stack[2].function}"
        )
        LOG.error(
            internal_message,
            stack_info=True,
            exc_info=assertion_error,
        )
    message: str = "No additional information was reported."
    if assertion_error.args and assertion_error.args[0]:
        message = assertion_error.args[0]
    new_error: JarsError = JarsError(
        message=f"{message}", error_code=HTTPStatus.INTERNAL_SERVER_ERROR
    )
    return handle_jars_errors(error=new_error)


def handle_jars_errors(error: JarsError) -> Response:
    LOG.error(
        f"JarsError: {error.message}",
        exc_info=error,
        stack_info=True,
    )
    return make_response(jsonify({"Error": error.message}), error.error_code)


def handle_internal_errors(error: InternalServerError) -> Response:
    original_error: Optional[BaseException] = error.original_exception
    if original_error:
        oe_type: str = str(type(original_error))
        LOG.error(
            msg=f"Internal Server Error based on {oe_type}",
            exc_info=original_error,
            stack_info=True,
        )
        if __debug__ is True:
            return make_response(
                jsonify({"Error": str(original_error)}),
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )
    return make_response(
        jsonify(
            {
                "Error": error.name,
                "Description": error.get_description(),
            }
        ),
        500,
    )


def handle_url_not_found(error) -> Response:
    message = "This URL is not recognized by the JARS API."
    LOG.warning(msg=message, exc_info=error)
    return make_response(jsonify({"Not Found": message}), HTTPStatus.NOT_FOUND)
