from flask import (
    Blueprint,
    render_template,
    request,
    jsonify
)

from services.fraud_service import (
    check_message
)


fraud_bp = Blueprint(
    "fraud",
    __name__
)


@fraud_bp.route(
    "/fraud-check"
)
def fraud_check():

    return render_template(
        "fraud_check.html"
    )


@fraud_bp.route(
    "/api/fraud/check",
    methods=["POST"]
)
def api_fraud_check():

    data = request.get_json(
        silent=True
    ) or {}


    message = data.get(
        "message",
        ""
    ).strip()


    if not message:

        return jsonify({
            "success": False,
            "message": "Enter a message."
        }), 400


    result = check_message(
        message
    )


    return jsonify({
        "success": True,
        **result
    })