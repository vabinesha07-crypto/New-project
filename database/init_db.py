import os
import sqlite3

from werkzeug.security import generate_password_hash

from config import Config


def get_connection():

    os.makedirs(
        os.path.dirname(Config.DATABASE_PATH),
        exist_ok=True
    )

    connection = sqlite3.connect(
        Config.DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection


def column_exists(
    cursor,
    table_name,
    column_name
):

    cursor.execute(
        f"PRAGMA table_info({table_name})"
    )

    columns = cursor.fetchall()

    return any(
        column["name"] == column_name
        for column in columns
    )


def add_column_if_missing(
    cursor,
    table_name,
    column_name,
    column_definition
):

    if not column_exists(
        cursor,
        table_name,
        column_name
    ):

        cursor.execute(
            f"""
            ALTER TABLE {table_name}
            ADD COLUMN {column_name}
            {column_definition}
            """
        )


def init_db():

    connection = get_connection()

    cursor = connection.cursor()


    # -----------------------------------------------------
    # USERS
    # -----------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            phone TEXT DEFAULT '',

            password_hash TEXT DEFAULT '',

            aadhaar TEXT DEFAULT '',

            community TEXT DEFAULT '',

            caste TEXT DEFAULT '',

            religion TEXT DEFAULT '',

            school_type TEXT DEFAULT '',

            created_at TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


    # -----------------------------------------------------
    # ADD MISSING USER COLUMNS
    # -----------------------------------------------------

    add_column_if_missing(
        cursor,
        "users",
        "password_hash",
        "TEXT DEFAULT ''"
    )

    add_column_if_missing(
        cursor,
        "users",
        "aadhaar",
        "TEXT DEFAULT ''"
    )

    add_column_if_missing(
        cursor,
        "users",
        "community",
        "TEXT DEFAULT ''"
    )

    add_column_if_missing(
        cursor,
        "users",
        "caste",
        "TEXT DEFAULT ''"
    )

    add_column_if_missing(
        cursor,
        "users",
        "religion",
        "TEXT DEFAULT ''"
    )

    add_column_if_missing(
        cursor,
        "users",
        "school_type",
        "TEXT DEFAULT ''"
    )


    # -----------------------------------------------------
    # SCHEMES
    # -----------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS schemes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            description TEXT,

            eligibility TEXT,

            benefits TEXT,

            documents TEXT,

            official_link TEXT
        )
        """
    )


    # -----------------------------------------------------
    # DOCUMENTS
    # -----------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            document_type TEXT,

            filename TEXT,

            filepath TEXT,

            status TEXT DEFAULT 'Uploaded',

            uploaded_at TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
        )
        """
    )


    # -----------------------------------------------------
    # APPLICATIONS
    # -----------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS applications (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            scheme_id INTEGER NOT NULL,

            status TEXT DEFAULT 'Saved',

            created_at TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id),

            FOREIGN KEY(scheme_id)
            REFERENCES schemes(id)
        )
        """
    )


    # -----------------------------------------------------
    # CREATE DEMO USER
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE LOWER(email) = LOWER(?)
        """,
        (
            "user@benefitshield.com",
        )
    )

    existing_user = cursor.fetchone()


    password_hash = generate_password_hash(
        "Benefit@123"
    )


    if existing_user:

        cursor.execute(
            """
            UPDATE users

            SET
                name = ?,
                password_hash = ?

            WHERE id = ?
            """,
            (
                "User",
                password_hash,
                existing_user["id"]
            )
        )

    else:

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
                "User",
                "user@benefitshield.com",
                "",
                password_hash
            )
        )


    # -----------------------------------------------------
    # DEFAULT SCHEMES
    # -----------------------------------------------------

    cursor.execute(
        """
        SELECT COUNT(*) AS count
        FROM schemes
        """
    )

    scheme_count = cursor.fetchone()["count"]


    if scheme_count == 0:

        schemes = [

            (
                "Post Matric Scholarship",
                "Financial assistance for eligible students pursuing higher education.",
                "Students meeting the applicable community, income and education requirements.",
                "Scholarship assistance according to the applicable scheme rules.",
                "Community Certificate, Income Certificate, Marksheet, Bonafide Certificate",
                "https://scholarships.gov.in/"
            ),

            (
                "Central Sector Scholarship",
                "Scholarship support for eligible students pursuing higher education.",
                "Eligibility depends on academic performance and applicable income criteria.",
                "Financial scholarship support.",
                "Income Certificate, Marksheet, Bonafide Certificate",
                "https://scholarships.gov.in/"
            ),

            (
                "National Means-cum-Merit Scholarship",
                "Educational scholarship support for eligible students.",
                "Eligibility depends on applicable examination, income and school criteria.",
                "Financial assistance for education.",
                "Income Certificate, School Certificate, Marksheet",
                "https://scholarships.gov.in/"
            )

        ]


        cursor.executemany(
            """
            INSERT INTO schemes
            (
                name,
                description,
                eligibility,
                benefits,
                documents,
                official_link
            )

            VALUES (?, ?, ?, ?, ?, ?)
            """,
            schemes
        )


    connection.commit()

    connection.close()