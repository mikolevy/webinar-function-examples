
def log_info(func):

    def wrapper(*args, **kwargs):
        print("Wywołuję funkcję...")
        result = func(*args, **kwargs)
        print("Już po wszystkim :)")
        return result

    return wrapper


@log_info
def calculate_sum(a, b):
    return a + b


def run_example():
    result = calculate_sum(10, 20)
    print(result)

    print(calculate_sum)
    print(calculate_sum.__name__)


if __name__ == '__main__':
    run_example()
