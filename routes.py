from flask import Blueprint, render_template

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return render_template("home/home.html")
