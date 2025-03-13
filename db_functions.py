from __init__db import *

def get_all_users() -> list:
    """
    :return: list[User]
    """
    session = next(get_db())
    result = session.query(User).all()
    return result

def add_user(response: dict) -> None:
    """
    :param response: dict{name: str, surname: str, patronymic: str, email: str}
    :return: None
    """
    session = next(get_db())
    new_user = User(
        first_name=response['name'],
        last_name=response['surname'],
        middle_name = response['patronymic'],
        email=response['email'],
        is_admin=False,
        confirmed = False,
    )
    new_user.set_password(response['password'])
    session.add(new_user)
    session.commit()

def is_confirmed(email: str) -> bool:
    """
    :param email: str
    :return: bool
    """
    session = next(get_db())
    user = session.query(User).filter_by(email=email).first()
    return user.confirmed

def is_existing(email: str) -> bool:
    """
    :param email: str
    :return: bool
    """
    session = next(get_db())
    user = session.query(User).filter_by(email=email).first()
    if user:
        return True
    return False

def set_confirmed(email: str) -> None:
    """
    :param email: str
    :return: None
    """
    session = next(get_db())
    user = session.query(User).filter_by(email=email).first()
    user.confirmed = 1
    session.commit()

print(is_existing('nikolas.kravtsov@gmail.com'))

