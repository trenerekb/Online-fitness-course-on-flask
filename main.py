from app import app
from app import db

from comments.blueprint import comments
from registration.registration import reg
from reports.report import report
from days.day import day

import view

app.register_blueprint(comments, url_prefix='/comments')
app.register_blueprint(reg, url_prefix='/registration')
app.register_blueprint(report, url_prefix='/report')
app.register_blueprint(day, url_prefix='/day')

if __name__ == "__main__":
    app.run()