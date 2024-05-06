from sqlalchemy import Column, String, Integer, Boolean, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'  # 1,1,         #1,2,3,4
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone_number = Column(Integer, unique=True)
    email = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


# Таблица карточек пользователя
class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_name = Column(String, nullable=False)
    card_number = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False, default=0)
    exp_date = Column(Integer, nullable=False)

    user_fk = relationship(User, lazy='subquery')


# Таблица переводов -> Транзакции
class Transfer(Base):
    __tablename__ = 'transfers'
    transfer_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_id = Column(Integer, ForeignKey("cards.card_id"))  # 1,2
    card_to_id = Column(Integer, nullable=False) # 5614 6818 1695 9195 (Пожертвования)
    amount = Column(Float, nullable=False)

    status = Column(Boolean, default=True)

    transaction_date = Column(DateTime)

    # Ботир если выйдет ошибка то поставь это  foreign_keys=[card_from_id], и обьясни им!
    card_from_fk = relationship(UserCard, lazy='subquery')
