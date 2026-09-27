import re


RULES = [

    (
        r"\botp\b",
        "Requests an OTP or verification code."
    ),

    (
        r"\bpin\b",
        "Requests a PIN."
    ),

    (
        r"pay\s*(₹|rs\.?|inr)?\s*\d+",
        "Requests an upfront payment."
    ),

    (
        r"processing fee",
        "Mentions a processing fee."
    ),

    (
        r"guaranteed approval",
        "Promises guaranteed approval."
    ),

    (
        r"send money",
        "Requests that money be sent."
    )

]


def analyze_message(
    message
):

    reasons = []


    for pattern, reason in RULES:

        if re.search(
            pattern,
            message,
            re.IGNORECASE
        ):

            reasons.append(
                reason
            )


    if len(reasons) >= 2:

        risk_level = "HIGH RISK"

        recommendation = (
            "Do not share OTPs, PINs or make a payment. "
            "Verify the information using the official scheme website."
        )


    elif len(reasons) == 1:

        risk_level = "MEDIUM RISK"

        recommendation = (
            "Pause before responding. "
            "Verify the sender and official website."
        )


    else:

        risk_level = "LOW RISK"

        recommendation = (
            "No common warning signs were detected. "
            "Still verify the sender before sharing information."
        )


    return {
        "risk_level": risk_level,
        "reasons": reasons,
        "recommendation": recommendation
    }