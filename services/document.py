from ai.ocr import extract_text

from ai.document_checker import (
    check_document
)

from models.document_model import (
    add_document
)

from models.user_model import (
    get_user
)


def process_document(
    file_path,
    file_name,
    document_type,
    user_id
):

    text = extract_text(
        file_path
    )


    user = get_user(
        user_id
    )


    user_name = ""

    if user:

        user_name = user["name"] or ""


    result = check_document(
        text,
        document_type,
        user_name
    )


    add_document(
        user_id,
        file_name,
        document_type,
        result["status"],
        result["summary"],
        text[:5000]
    )


    return result