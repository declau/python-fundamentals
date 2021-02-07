def super_secret_function(f):
    return f


@super_secret_function
def my_function():
    print("This is my secret function.")


print(my_function())


print("--------------------------------------------------------")

# This is the decorator
def print_args(func):
    def inner_func(*args, **kwargs):
        print("args", args)
        print("kargs", kwargs)
        return func(*args, **kwargs)  # Call the original function with its arguments.

    return inner_func


@print_args
def multiply(num_a, num_b):
    return num_a * num_b


print(multiply(3, 5))
# Output:
# (3,5) - This is actually the 'args' that the function receives.
# {} - This is the 'kwargs', empty because we didn't specify keyword arguments.
# 15 - The result of the function