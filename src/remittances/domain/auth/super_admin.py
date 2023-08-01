from functools import wraps
from flask import g, abort
from flask_security import current_user


def super_admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(401)  # No está autenticado
        if not current_user.has_role('super_admin'):
            abort(403)  # No tiene permisos
        return f(*args, **kwargs)
    return decorated_function
