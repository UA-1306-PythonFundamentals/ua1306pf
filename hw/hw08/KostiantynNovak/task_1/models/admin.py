def new_admin():
    name = "new_name"
    return name


def create_admin():
    b_name = new_admin()
    return b_name

__all__ = ['create_admin']