from flask import render_template, Blueprint

app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/")
def index():
    from models import Shop
    from main import db

    data = db.session.query(Shop).all()

    return render_template("index.html", data=data)

