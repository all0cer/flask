
from flask import Flask
from delivery.exts import site
from delivery.exts import db
from delivery.exts import cli
from delivery.exts import config
from delivery.exts import migrates

def create_app():
    app =  Flask(__name__) 
    config.init_app(app)
    db.init_app(app)
    migrates.init_app(app)
    cli.init_app(app)
    site.init_app(app)
    return app

