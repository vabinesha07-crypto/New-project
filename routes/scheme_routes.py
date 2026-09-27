from flask import (
    Blueprint,
    render_template,
    request,
    abort
)

from services.scheme_service import (
    search_schemes,
    scheme_details
)


scheme_bp = Blueprint(
    "schemes",
    __name__,
    url_prefix="/schemes"
)


@scheme_bp.route("/")
def schemes():

    query = request.args.get(
        "q",
        ""
    ).strip()


    schemes = search_schemes(
        query
    )


    return render_template(
        "schemes.html",
        schemes=schemes,
        query=query
    )


@scheme_bp.route(
    "/<int:scheme_id>"
)
def scheme_detail(
    scheme_id
):

    scheme = scheme_details(
        scheme_id
    )


    if not scheme:

        abort(404)


    return render_template(
        "scheme_details.html",
        scheme=scheme
    )