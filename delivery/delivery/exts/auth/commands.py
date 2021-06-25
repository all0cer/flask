import click
from delivery.exts.db import db
from delivery.exts.auth.model_user import User 


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