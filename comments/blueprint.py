from flask import Blueprint, render_template


comments = Blueprint('comments', __name__, template_folder='templates')


@comments.route('/')
def index():
    return render_template('comments/index.html')