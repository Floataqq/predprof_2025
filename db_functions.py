from __init__db import User

def get_all_users() -> list:
    result = User.query().all()
    return result


