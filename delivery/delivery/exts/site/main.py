from flask import render_template
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/promoções")
def promocoes():
    return render_template("promocoes.html")

