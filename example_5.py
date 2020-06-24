
def log_info(func):

    def wrapper():
        print("Wywołuję funkcję...")
        func()
        print("Już po wszystkim :)")
    return wrapper


def say_hello():
    print("Hello World!")


def run_example():
    say_hello_with_log_info = log_info(say_hello)
    say_hello_with_log_info()


if __name__ == '__main__':
    run_example()
