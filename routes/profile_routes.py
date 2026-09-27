from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from models.user_model import (
    get_user,
    get_user_by_email,
    update_user_profile
)


profile_bp = Blueprint(
    "profile",
    __name__
)


@profile_bp.route(
    "/profile",
    methods=["GET", "POST"]
)
def profile():

    if "user_id" not in session:

        return redirect(
            url_for("auth.login")
        )

    user_id = session["user_id"]

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        phone = request.form.get(
            "phone",
            ""
        ).strip()

        aadhaar = request.form.get(
            "aadhaar",
            ""
        ).strip()

        community = request.form.get(
            "community",
            ""
        ).strip()

        caste = request.form.get(
            "caste",
            ""
        ).strip()

        religion = request.form.get(
            "religion",
            ""
        ).strip()

        school_type = request.form.get(
            "school_type",
            ""
        ).strip()

        if not name:

            flash(
                "Name is required.",
                "error"
            )

            return redirect(
                url_for("profile.profile")
            )

        existing_user = get_user_by_email(
            email
        )

        if (
            existing_user
            and existing_user["id"] != user_id
        ):

            flash(
                "That email address is already in use.",
                "error"
            )

            return redirect(
                url_for("profile.profile")
            )

        update_user_profile(
            user_id,
            name,
            email,
            phone,
            aadhaar,
            community,
            caste,
            religion,
            school_type
        )

        flash(
            "Profile updated successfully.",
            "success"
        )

        return redirect(
            url_for("profile.profile")
        )

    user = get_user(user_id)

    return render_template(
        "profile.html",
        user=user
    )