from enum import Flag
import click
from delivery.exts.db import db
from delivery.exts.db import models


def init_app(app):

    @app.cli.command()
    def create_db():
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_new_user(email, passwd, admin):
        user = User(
            email = email,
            passwd = passwd,
            admin = admin
        )
        db.session.add(user)
        db.session.commit()