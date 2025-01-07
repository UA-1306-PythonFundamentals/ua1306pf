def func_a():
    a = 10
    return a



def create_user():
    new_user_id = func_a()
    return new_user_id


__all__ = ['create_user']