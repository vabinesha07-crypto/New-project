from database.init_db import get_connection


def get_schemes(query=""):

    connection = get_connection()


    if query:

        schemes = connection.execute(
            """
            SELECT *
            FROM schemes

            WHERE
                name LIKE ?
                OR category LIKE ?
                OR description LIKE ?

            ORDER BY id
            """,
            (
                f"%{query}%",
                f"%{query}%",
                f"%{query}%"
            )
        ).fetchall()


    else:

        schemes = connection.execute(
            """
            SELECT *
            FROM schemes
            ORDER BY id
            """
        ).fetchall()


    connection.close()

    return schemes


def get_scheme(scheme_id):

    connection = get_connection()

    scheme = connection.execute(
        """
        SELECT *
        FROM schemes
        WHERE id = ?
        """,
        (
            scheme_id,
        )
    ).fetchone()

    connection.close()

    return scheme