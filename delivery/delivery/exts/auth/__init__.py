from delivery.exts.auth import model_user #noqa
from delivery.exts.auth.commands import add_new_user
from delivery.exts.admin import admin
from delivery.exts.auth.admin_view import UserAdmin
from delivery.exts.db import db
from delivery.exts.auth.model_user import User


def init_app(app):
    app.cli.command()(add_new_user)

    admin.add_view(UserAdmin(User, db.session))