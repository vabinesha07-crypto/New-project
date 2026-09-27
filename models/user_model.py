import sqlite3

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from config import Config


def get_connection():

    connection = sqlite3.connect(
        Config.DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection


def get_user(user_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    connection.close()

    if user:

        return dict(user)

    return None


def get_user_by_email(email):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE LOWER(email) = LOWER(?)
        """,
        (
            email.strip(),
        )
    )

    user = cursor.fetchone()

    connection.close()

    if user:

        return dict(user)

    return None


def verify_user(
    email,
    password
):

    user = get_user_by_email(
        email
    )

    if not user:

        return None


    password_hash = user.get(
        "password_hash"
    )


    if not password_hash:

        return None


    try:

        if check_password_hash(
            password_hash,
            password
        ):

            return user

    except Exception:

        return None


    return None


def create_user(
    name,
    email,
    password,
    phone=""
):

    password_hash = generate_password_hash(
        password
    )

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (
            name,
            email,
            phone,
            password_hash
        )

        VALUES (?, ?, ?, ?)
        """,
        (
            name,
            email,
            phone,
            password_hash
        )
    )

    connection.commit()

    user_id = cursor.lastrowid

    connection.close()

    return user_id


def update_profile(
    user_id,
    name,
    phone,
    aadhaar,
    community,
    caste,
    religion,
    school_type
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users

        SET
            name = ?,
            phone = ?,
            aadhaar = ?,
            community = ?,
            caste = ?,
            religion = ?,
            school_type = ?

        WHERE id = ?
        """,
        (
            name,
            phone,
            aadhaar,
            community,
            caste,
            religion,
            school_type,
            user_id
        )
    )

    connection.commit()

    connection.close()


def update_password(
    user_id,
    password
):

    password_hash = generate_password_hash(
        password
    )

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users

        SET password_hash = ?

        WHERE id = ?
        """,
        (
            password_hash,
            user_id
        )
    )

    connection.commit()

    connection.close()