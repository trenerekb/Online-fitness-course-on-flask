from app import app
from days.day import day
from profiles.profile import profile
from registration.registration import reg
from reports.report import report
from results.results_clients import result

app.register_blueprint(reg, url_prefix='/registration')
app.register_blueprint(report, url_prefix='/report')
app.register_blueprint(day, url_prefix='/day')
app.register_blueprint(result, url_prefix='/result')
app.register_blueprint(profile, url_prefix='/profile')

if __name__ == "__main__":
    app.run()