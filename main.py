from app import app
from app import db

from comments.blueprint import comments

import view

app.register_blueprint(comments, url_prefix='/comments')


if __name__ == "__main__":
    app.run()