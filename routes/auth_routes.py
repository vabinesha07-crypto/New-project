from functools import wraps

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
    verify_user,
    update_profile
)


auth_bp = Blueprint(
    "auth",
    __name__
)


def login_required(view_function):

    @wraps(view_function)
    def wrapped_view(*args, **kwargs):

        if not session.get("user_id"):

            flash(
                "Please login to continue.",
                "error"
            )

            return redirect(
                url_for("auth.login")
            )

        return view_function(
            *args,
            **kwargs
        )

    return wrapped_view


@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )


        if not email or not password:

            flash(
                "Please enter both email and password.",
                "error"
            )

            return render_template(
                "login.html"
            )


        user = verify_user(
            email,
            password
        )


        if not user:

            flash(
                "Invalid email or password.",
                "error"
            )

            return render_template(
                "login.html"
            )


        session.clear()

        session["user_id"] = user["id"]


        flash(
            "Login successful.",
            "success"
        )


        return redirect(
            url_for("dashboard")
        )


    return render_template(
        "login.html"
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    flash(
        "You have been logged out.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )


@auth_bp.route(
    "/profile",
    methods=["GET", "POST"]
)
@login_required
def profile():

    user_id = session.get(
        "user_id"
    )

    user = get_user(
        user_id
    )


    if not user:

        session.clear()

        return redirect(
            url_for("auth.login")
        )


    if request.method == "POST":

        name = request.form.get(
            "name",
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

            return render_template(
                "profile.html",
                user=user
            )


        update_profile(
            user_id,
            name,
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
            url_for("auth.profile")
        )


    return render_template(
        "profile.html",
        user=user
    )