"""
Instructions
Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was given
and finllay the returned ouput:

You called a_function(1,2,3)
It returned: 6

The value 6 is the return value of the function.  Don't change the body of a_function.

IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.

You can use function __name__ to get the name of the function.
"""
#inputs [1,2,3]
inputs = eval(input())
print(inputs)
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
  def wrapper(*args):
    print(f"You called {function.__name__}{args}")
    result = function(args[0], args[1], args[2])
    print(f"It returned: {result}")
  return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])