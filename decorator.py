def my_decorator(func):
    def wrapper(a, b):
        print("Before Addition")
        result = func(a, b)
        print("After Addition")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(6 , 3)
print(result)