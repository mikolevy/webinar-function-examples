
def log_info(func):

    def wrapper():
        print("Wywołuję funkcję...")
        func()
        print("Już po wszystkim :)")
    return wrapper


@log_info
def say_hello():
    print("Hello World!")


def run_example():
    say_hello()


if __name__ == '__main__':
    run_example()
