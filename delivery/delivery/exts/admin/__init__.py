from delivery.exts import db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from delivery.exts.db.models import Category
from delivery.exts.db import db


admin = Admin()

def init_app(app):
    admin.name = ("ADMINNAME" "PyFoods")
    admin.template_mode = ("TEMPLATES_MODE" "bootstrap2")
    admin.init_app(app)

    admin.add_view(ModelView(Category, db.session))