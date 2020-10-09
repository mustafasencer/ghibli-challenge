from functools import wraps

from app import redis_client


def cache(ttl=30):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            films = redis_client.get('films')
            if not films:
                films = f(*args, **kw)
                redis_client.set('films', films, ex=ttl)
            return films

        return wrapper

    return decorator
