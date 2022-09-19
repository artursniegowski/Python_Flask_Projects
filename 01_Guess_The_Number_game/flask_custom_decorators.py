# decorators for adding html tags as well as some inline CSS styling !
# https://docs.python.org/3/library/functools.html#functools.wraps
from functools import wraps

# decorator for adding html img tag
def add_html_img(src:str = None):
    """adds img html tag with the given src"""
    def outter_wrapper(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            if not src:
                return fn(*args,**kwargs)
            else:
                return fn(*args,**kwargs) + f"<img src='{src}'>"
        return wrapper
    return outter_wrapper

# decorator for adding html tag and some styling
def add_html_tag(tag:str = None, inline_style:str = None):
    """adds html tag and style """
    def outter_wrapper(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            if not tag:
                return fn(*args,**kwargs)
            else:
                if inline_style:
                    return f"<{tag} style='{inline_style}'>" + fn(*args,**kwargs) + f"</{tag}>"
                else:
                    return f"<{tag}>" + fn(*args,**kwargs) + f"</{tag}>"
        return wrapper
    return outter_wrapper
