from database.init_db import get_connection


def create_application(
    user_id,
    scheme_id
):

    connection = get_connection()

    existing = connection.execute(
        """
        SELECT id
        FROM applications
        WHERE user_id = ?
        AND scheme_id = ?
        """,
        (
            user_id,
            scheme_id
        )
    ).fetchone()


    if not existing:

        connection.execute(
            """
            INSERT INTO applications
            (
                user_id,
                scheme_id,
                status,
                progress
            )

            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                scheme_id,
                "Documents pending",
                25
            )
        )

        connection.commit()


    connection.close()


def get_applications(user_id):

    connection = get_connection()

    applications = connection.execute(
        """
        SELECT
            applications.id,
            applications.user_id,
            applications.scheme_id,
            applications.status,
            applications.progress,
            applications.created_at,
            schemes.name AS scheme_name,
            schemes.category AS scheme_category

        FROM applications

        LEFT JOIN schemes
        ON applications.scheme_id = schemes.id

        WHERE applications.user_id = ?

        ORDER BY applications.created_at DESC
        """,
        (
            user_id,
        )
    ).fetchall()


    connection.close()

    return applications