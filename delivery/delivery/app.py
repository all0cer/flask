
from flask import Flask
from delivery.exts import site
from delivery.exts import db
from delivery.exts import cli
from delivery.exts import config
from delivery.exts import migrates
from delivery.exts import auth
from delivery.exts import admin

def create_app():
    app =  Flask(__name__) 
    config.init_app(app)
    #Abaixo se iniciam pelo Dynaconf em settings.toml
    return app

