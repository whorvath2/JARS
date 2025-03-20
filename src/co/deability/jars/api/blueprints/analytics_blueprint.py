from http import HTTPStatus
from typing import Final, Tuple

from flask import Blueprint, make_response, request

from co.deability.jars.service import analytics_service


analytics_blueprint: Blueprint = Blueprint(
    "analytics", __name__, url_prefix="/lirs/analytics"
)

EMPTY_SUCCESS_RESPONSE: Final[Tuple[str, int]] = ("", HTTPStatus.NO_CONTENT)


@analytics_blueprint.post("/run/rscript")
def post_script():
    return make_response(
        str(analytics_service.run(script=request.get_data(as_text=True))), HTTPStatus.OK
    )
