import os

from flask import Blueprint, render_template
from flask_login import login_required, current_user

from config import Configuration
from models import Client, Day, Report, Result

day = Blueprint('days', __name__, template_folder='templates')


@day.route('/<day_number>')
@login_required
def day_marathon(day_number):
    client_id = current_user.id
    current_day = Day.query.filter(Day.id == int(day_number) + 1).first()
    client_data = Client.query.filter(Client.id == client_id).first()
    count_days = [i for i in range(int(Day.query.count()))]
    all_reports = Report.query.filter(Report.day_id == day_number)
    client_report = Report.query.filter(Report.client_id == client_id, Report.day_id == day_number).first()
    video = os.path.join(Configuration.path_to_video_and_cover, current_day.video_path)
    cover_video = os.path.join(Configuration.path_to_video_and_cover, current_day.cover_video_path)
    result = Result.query.filter(Result.day_id == day_number, Result.client_id == client_id).first()

    if day_number in ('0', '7', '14', '21'):
        return render_template('days/measurement_day.html', client_data=client_data, video=video, result=result,
                               cover_video=cover_video, client_report=client_report,
                               day=current_day, count_days=count_days, title=f'День {day_number}')

    return render_template('days/day.html', video=video, cover_video=cover_video, client_data=client_data,
                           client_report=client_report, day=current_day, all_reports=all_reports,
                           count_days=count_days, title=f'День {day_number}')
