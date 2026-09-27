MESSAGES = {

    "en": {

        "document_ok":
            "Your document passed the basic checks.",

        "fraud_warning":
            "Please verify the message before taking action."

    },


    "ta": {

        "document_ok":
            "உங்கள் ஆவணம் அடிப்படை சரிபார்ப்பில் தேர்ச்சி பெற்றுள்ளது.",

        "fraud_warning":
            "நடவடிக்கை எடுப்பதற்கு முன் செய்தியை சரிபார்க்கவும்."

    }

}


def get_message(
    key,
    language="en"
):

    language_messages = MESSAGES.get(
        language,
        MESSAGES["en"]
    )


    return language_messages.get(
        key,
        ""
    )