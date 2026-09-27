import re


def valid_email(
    email
):

    pattern = (
        r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    )

    return bool(
        re.match(
            pattern,
            email
        )
    )


def valid_aadhaar(
    aadhaar
):

    return (
        aadhaar.isdigit()
        and len(aadhaar) == 12
    )


def valid_phone(
    phone
):

    digits = "".join(
        character
        for character in phone
        if character.isdigit()
    )

    return len(digits) == 10