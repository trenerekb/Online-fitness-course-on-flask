from flask import Blueprint, render_template, url_for, request, flash, session, redirect, abort
from flask_login import login_required, current_user

from models import Client, Day

day = Blueprint('day', __name__, template_folder='templates')


@day.route('/<day_number>')
@login_required
def day_marathon(day_number):
    day = Day.query.filter_by(id=int(day_number)+1).first()
    count_days = [i for i in range(int(Day.query.count()))]
    path_storage = 'storage/marathon_days/'
    if day_number == '0':
        return render_template('days/day0.html', path_storage=path_storage, day=day, count_days=count_days)
    else:
        return render_template('days/day.html', path_storage=path_storage, day=day, count_days=count_days,
                               current_user=current_user)


@day.route('/quiz', methods=['POST', 'GET'])
def quiz():
    if request.method == 'POST':
        growth = request.form.get('growth')
        weight = request.form.get('weight')
        date_birth = request.form.get('date_birth')
        hand = request.form.get('hand')
        thorax = request.form.get('thorax')
        waist = request.form.get('waist')
        abdomen = request.form.get('abdomen')
        buttocks = request.form.get('buttocks')
        thigh = request.form.get('thigh')
        print(growth, weight, date_birth, hand, thorax, waist, abdomen, buttocks, thigh)
        flash('Отлично!', category='right')
    return redirect(url_for('day_marathon', day_number='0'))