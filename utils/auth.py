from models.scheme_model import (
    get_schemes,
    get_scheme
)


def search_schemes(
    query=""
):

    return get_schemes(
        query
    )


def scheme_details(
    scheme_id
):

    return get_scheme(
        scheme_id
    )