import functools


def require_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('user_role') != 'admin':
            return {"error": "Admin access required."}
        return func(*args, **kwargs)
    return wrapper