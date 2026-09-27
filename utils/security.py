from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


def hash_password(
    password
):

    return generate_password_hash(
        password
    )


def verify_password(
    password_hash,
    password
):

    try:

        return check_password_hash(
            password_hash,
            password
        )

    except Exception:

        return False