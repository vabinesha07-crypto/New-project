import os
import uuid

from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    session
)

from werkzeug.utils import secure_filename

from config import Config

from models.document_model import (
    get_documents
)

from services.document import (
    process_document
)

from utils.auth import login_required


document_bp = Blueprint(
    "documents",
    __name__
)


@document_bp.route(
    "/documents"
)
@login_required
def documents():

    documents = get_documents(
        session["user_id"]
    )

    return render_template(
        "documents.html",
        documents=documents
    )


@document_bp.route(
    "/documents/check"
)
@login_required
def document_check():

    return render_template(
        "document_check.html"
    )


@document_bp.route(
    "/api/document/check",
    methods=["POST"]
)
@login_required
def api_document_check():

    if "document" not in request.files:

        return jsonify({
            "success": False,
            "message": "Please choose a document."
        }), 400


    file = request.files["document"]


    if not file.filename:

        return jsonify({
            "success": False,
            "message": "Please choose a document."
        }), 400


    filename = secure_filename(
        file.filename
    )


    extension = (
        os.path.splitext(
            filename
        )[1]
        .lower()
        .replace(
            ".",
            ""
        )
    )


    if extension not in Config.ALLOWED_EXTENSIONS:

        return jsonify({
            "success": False,
            "message": "This file type is not supported."
        }), 400


    unique_name = (
        f"{uuid.uuid4().hex}_{filename}"
    )


    file_path = os.path.join(
        Config.UPLOAD_FOLDER,
        unique_name
    )


    file.save(
        file_path
    )


    document_type = request.form.get(
        "document_type",
        "Other Files"
    )


    result = process_document(
        file_path,
        unique_name,
        document_type,
        session["user_id"]
    )


    return jsonify({
        "success": True,
        "status": result["status"],
        "summary": result["summary"],
        "checks": result["checks"]
    })