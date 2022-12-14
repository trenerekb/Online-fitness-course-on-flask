# Body Home
![Python 3.10.1](https://img.shields.io/badge/python-3.10.1-brightgreen) ![flask-2.2.3](https://img.shields.io/badge/flask-2.2.3-brightgreen)
![Flask-Migrate-3.1](https://img.shields.io/badge/flask_migrate-3.1-brightgreen)

![Flask-ADMin-1.6](https://img.shields.io/badge/flask_admin-1.6.0-brightgreen)
![jinja2](https://img.shields.io/badge/jinja-2-yellowgreen)
![HTML](https://img.shields.io/badge/html-5-yellowgreen)
![css](https://img.shields.io/badge/css-yellowgreen)
![JavaScript](https://img.shields.io/badge/JavaScript-yellowgreen)


**Body Home** - это веб приложение для женщин, которые хотят похудеть в домашних условиях.

## **Что реализовано**

**1. Страница одного из дней в онлайн курсе, в которой можно:**
+ [X] Просмотром видео тренировки или лекции по питанию.
+ [X] Добавление своего отчета (текст и фото своей еды).
+ [X] Редактирование и/или удаление своего отчета.
+ [X] Добавление комментария к отчету.
+ [X] Добавление лайков :+1: к отчету через js(fetch())
+ [X] Удобная навигация по дням курса с помощью адаптивного меню.
+ [X] Просмотр отчетов других участниц в этом дне.

*Просмотр видео*
![day](days/day_of_course.png)
<br>
<br>
*Добавлеине отчетов, комментариев, лайков*
![report](reports/add_report.png)
##

**2. Сбор и сохранение замеров:**
+ [X] Меняющиеся формы сделаны на js.

![results](results/measurements.png)
<br>
<br>
##

**3. Профиль клиента, где есть:**
+ [X] Возможность загрузить свой аватар.
+ [X] Посмотреть на таблицу с замерами и увидеть свои результаты.
+ [X] Разместить фото "ДО ПОСЛЕ".

 ![profile](profiles/profile.png)
<br>
<br>
##

**4. Админ панель, в которой можно:**
+ [X] Просматривать| добавлять| удалять| редактировать всех пользователей из БД. А так же менять роль с studen на admin.
+ [X] Создавать новые дни в онлайн курсу: добавлять новые видео, описание, задание.
+ [X] Просмотривать| удалять клиентские отчеты.

 ![admin](admin/admin_panel.png)
<br>
<br>
##

**5. Регистрация новых пользователей:**
+ [X] Проверка через flask-security.
+ [X] Создание hash pasword.

![registration](registration/registration.png)
<br>
<br>
##

**6. Создание БД и связи между таблицами:**
+ [X] Использовал flask-sqlalchemy.
+ [X] Добавление новых таблиц и связей flask-migrate.

![registration](db.png)
##
