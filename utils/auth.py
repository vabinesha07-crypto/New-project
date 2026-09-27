from functools import wraps

from flask import (
    session,
    redirect,
    url_for,
    flash
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
                url_for(
                    "auth.login",
                    next="/dashboard"
                )
            )

        return view_function(
            *args,
            **kwargs
        )

    return wrapped_view