import functools
from dataclasses import dataclass


@dataclass
class Request:
    is_authenticated: bool


def auth_check(require: bool):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(request: Request, *args, **kwargs):
            if require and not request.is_authenticated:
                raise Exception("Auth is required!")
            return func(request, *args, **kwargs)

        return wrapper
    return decorator


@auth_check(require=False)
def get_students_names(request: Request):
    return [
        "Alicja",
        "Jakub",
        "Mikołaj",
        "Dorota"
    ]


def run_example():
    # request = Request(is_authenticated=True)
    request = Request(is_authenticated=False)
    print(get_students_names(request))


if __name__ == '__main__':
    run_example()
