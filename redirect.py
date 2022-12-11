from flask import render_template, url_for, redirect

from app import app


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('registration.login'))

    return response


@app.errorhandler(404)
def page_not_fount(error):
    return render_template('page404.html', title='Старница не найдена')
