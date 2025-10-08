def simple_decorator(func):
    def wrapper():
        print("Starting function")
        func()
        print("Function completed")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()