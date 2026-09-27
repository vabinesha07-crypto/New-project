import os

from flask import Flask, render_template, session

from config import Config
from database.init_db import init_db
from models.user_model import get_user

from routes.auth_routes import auth_bp
from routes.scheme_routes import scheme_bp
from routes.document_routes import document_bp
from routes.fraud_routes import fraud_bp
from routes.application_routes import application_bp


app = Flask(__name__)

app.config.from_object(Config)

app.secret_key = app.config["SECRET_KEY"]

os.makedirs(
    app.config["UPLOAD_FOLDER"],
    exist_ok=True
)


# ---------------------------------------------------------
# INITIALIZE DATABASE
# ---------------------------------------------------------

init_db()


# ---------------------------------------------------------
# REGISTER BLUEPRINTS
# ---------------------------------------------------------

app.register_blueprint(auth_bp)
app.register_blueprint(scheme_bp)
app.register_blueprint(document_bp)
app.register_blueprint(fraud_bp)
app.register_blueprint(application_bp)


# ---------------------------------------------------------
# CURRENT USER
# ---------------------------------------------------------

@app.context_processor
def inject_user():

    user = None

    user_id = session.get("user_id")

    if user_id:

        user = get_user(user_id)

        if user is None:
            session.clear()

    return {
        "current_user": user
    }


# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ---------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------

@app.route("/dashboard")
def dashboard():

    from flask import redirect, url_for

    if not session.get("user_id"):

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "dashboard.html"
    )


# ---------------------------------------------------------
# HELP
# ---------------------------------------------------------

@app.route("/help")
def help_page():

    return render_template(
        "help.html"
    )


# ---------------------------------------------------------
# 404 ERROR
# ---------------------------------------------------------

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "help.html"
    ), 404


# ---------------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )