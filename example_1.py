
def say_hello():
    print("Hello World!")


def say_name(name):
    print(f"Hello {name}!")


def calculate_something(some_value, other_value):
    return some_value + other_value


def run_example():
    hello_func = say_hello
    hello_func()

    hello_name = say_name
    hello_name("Mikołaj")
    #
    calculation = calculate_something
    result = calculation(10, 30)
    print(result)


if __name__ == '__main__':
    run_example()
