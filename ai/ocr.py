import os


def extract_text(
    file_path
):

    extension = os.path.splitext(
        file_path
    )[1].lower()


    try:

        if extension == ".pdf":

            import fitz

            document = fitz.open(
                file_path
            )


            text = ""


            for page in document:

                text += page.get_text()


            document.close()


            return text.strip()


        from PIL import Image

        import pytesseract


        image = Image.open(
            file_path
        )


        text = pytesseract.image_to_string(
            image
        )


        return text.strip()


    except Exception:

        return ""