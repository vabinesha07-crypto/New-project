import os


def allowed_file(
    filename,
    allowed_extensions
):

    if not filename:

        return False


    extension = os.path.splitext(
        filename
    )[1].lower().replace(
        ".",
        ""
    )


    return extension in allowed_extensions