from delivery.exts import db
from .migrate import migrate
from delivery.exts.db import db

def init_app(app):
    migrate.init_app(app, db)