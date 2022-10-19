# decorators for checking if the current_user is the admin
# otherwise: HTTP 403 Forbidden response
# https://docs.python.org/3/library/functools.html#functools.wraps
from flask import abort
from flask_login import current_user
from functools import wraps

# checking if current user is admin , id == 1, otherwise: HTTP 403 Forbidden response 
def admin_only(fn):
    """
    checking if current user is admin , id == 1, otherwise: HTTP 403 Forbidden response
    """
    @wraps(fn)
    def decorated_function(*args,**kwargs):
        if current_user.is_authenticated:
            if current_user.id == 1:
                return fn(*args,**kwargs)
    
        # HTTP 403 - Forbidden response
        return abort(403)
    return decorated_function
