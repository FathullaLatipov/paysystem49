from fastapi import APIRouter
import re
from database.userservice import registration_user_db, get_exact_user_db, get_all_users_db, edit_user_db, \
    check_user_phone_db

from pydantic import BaseModel

user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])


# Регистрация
class UserRegistrationValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    country: str


# Если выйдет ошибка Ботир то дайте капзду Айдосу и Ойбеку(Голубой) и Азиз(Чушпану)
@user_router.post('/register')
async def register_new_user(data: UserRegistrationValidator):
    # Ботир обьясни это model_dump() мне лень
    new_user_data = data.model_dump()

    regex = re.match(r'^(\+998|998)\d{9}$', new_user_data.phone_number)
    # sdfasdf
    if regex:
        return True
    else:
        return False