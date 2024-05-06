from database.models import User
from database import get_db

from datetime import datetime


# Регистрация
def registration_user_db(name, surname, email, phone_number, country, password, reg_date):
    db = next(get_db())

    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number,
                    country=country, password=password, reg_date=datetime.now())
    db.add(new_user)
    db.commit()

    return f'Такой пользователь {name} успешно прошел регистрацию!'


# Получить инфо о пользователе
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return 'У нас в базе нету такого пользователя(('


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


# Проверка данных через phone_number(validate)
def check_user_phone_db(phone_number):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return checker
    else:
        return 'У нас в базе нету тaкого номера телефона((('


# Изменить данные у определенного пользователя(id)
def edit_user_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_info == 'email':
            exact_user.email = new_info
        elif edit_info == 'country':
            exact_user.country = new_info

        db.commit()

        return f'Данные у этого {user_id} был успешно изменен!'
    else:
        return 'У нас в базе нету такого пользователя((('


# Удаления пользователя
# 3мин
