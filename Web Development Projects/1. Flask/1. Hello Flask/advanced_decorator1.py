
def decorator(function):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        function(*args, **kwargs)
    return wrapper

@decorator
def suma(a, b, c):
    print(f"La suma es {a + b + c}")

suma(1,2,3)