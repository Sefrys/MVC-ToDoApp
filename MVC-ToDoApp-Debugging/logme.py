"""Logging decorator function, decorate with @logme"""
from functools import wraps


def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("Called {} with args {} and kwargs {}".format(
                func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return inner
