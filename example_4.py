import random


def say_hello():
    print("Hello World!")


def say_surprise():
    print("Surprise!")


def surprise(func):
    number = random.randint(1, 3)
    if number > 2:
        return func
    return say_surprise


def run_example():
    surprise_func = surprise(say_hello)
    surprise_func()


if __name__ == '__main__':
    run_example()
