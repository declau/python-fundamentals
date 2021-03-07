# Errors and Exceptions

# x = -5

# if x < 0:
#     raise Exception("x should be positive")


# y = -5
# assert y >= 0, "y is not positive!"

# try:
#     a = 5 / 0
# except:
#     print("an error happened")

# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)

# try:
#     a = 5 / 0
# except ZeroDivisionError:
#     print()

try:
    a = 5 / 1
    b = a + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine!")
finally:
    print("cleaning up...")


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError("Value is too small", x)


try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)