from database.init_db import get_connection


def add_document(
    user_id,
    file_name,
    document_type,
    status,
    result,
    extracted_text
):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO documents
        (
            user_id,
            file_name,
            document_type,
            status,
            result,
            extracted_text
        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            file_name,
            document_type,
            status,
            result,
            extracted_text
        )
    )

    connection.commit()

    connection.close()


def get_documents(user_id):

    connection = get_connection()

    documents = connection.execute(
        """
        SELECT *
        FROM documents

        WHERE user_id = ?

        ORDER BY id DESC
        """,
        (
            user_id,
        )
    ).fetchall()

    connection.close()

    return documents