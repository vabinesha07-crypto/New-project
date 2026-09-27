from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from models.application_model import (
    create_application,
    get_applications
)

from utils.auth import login_required


application_bp = Blueprint(
    "applications",
    __name__
)


@application_bp.route(
    "/applications"
)
@login_required
def applications():

    user_id = session.get(
        "user_id"
    )

    applications = get_applications(
        user_id
    )

    return render_template(
        "applications.html",
        applications=applications
    )


@application_bp.route(
    "/applications/create",
    methods=["POST"]
)
@login_required
def create():

    scheme_id = request.form.get(
        "scheme_id",
        type=int
    )


    if not scheme_id:

        flash(
            "Invalid scheme.",
            "error"
        )

        return redirect(
            url_for(
                "schemes.schemes"
            )
        )


    create_application(
        session["user_id"],
        scheme_id
    )


    flash(
        "Scheme added to your applications.",
        "success"
    )


    return redirect(
        url_for(
            "applications.applications"
        )
    )