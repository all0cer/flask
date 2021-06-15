from delivery.exts.db import db

def init_app(app):

    @app.cli.command()
    def create_db():
        db.create_all()