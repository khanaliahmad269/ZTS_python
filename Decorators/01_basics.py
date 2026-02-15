from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before The function runs")
        func()
        print("After the Function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello!! Welcome to ZTS python course!!")

greet()
print(greet.__name__)