from flask import Blueprint, render_template
from models.users import get_user_by_id

app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/')
def index():
    return render_template("home/home.html")
