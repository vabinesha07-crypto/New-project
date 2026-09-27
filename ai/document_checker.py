def check_document(
    text,
    document_type,
    user_name=""
):

    text = text or ""

    checks = []


    checks.append({
        "label": "Document detected",
        "ok": bool(
            text.strip()
        )
    })


    checks.append({
        "label": "Information is readable",
        "ok": len(
            text.strip()
        ) >= 20
    })


    name_match = False


    if user_name:

        user_parts = (
            user_name.lower()
            .split()
        )


        document_text = (
            text.lower()
        )


        for part in user_parts:

            if (
                len(part) > 2
                and part in document_text
            ):

                name_match = True

                break


    checks.append({
        "label": "Name appears in document",
        "ok": name_match
    })


    if not text.strip():

        status = "Needs Attention"

        summary = (
            "The document could not be read. "
            "Try uploading a clearer image or PDF."
        )


    elif len(text.strip()) < 20:

        status = "Needs Attention"

        summary = (
            "The file was opened, but there is "
            "not enough readable text."
        )


    elif not name_match:

        status = "Needs Attention"

        summary = (
            "The document is readable, but the "
            "profile name could not be matched."
        )


    else:

        status = "Looks OK"

        summary = (
            "The basic document checks passed. "
            "Confirm the final requirements on the official website."
        )


    return {
        "status": status,
        "summary": summary,
        "checks": checks
    }