class MyCustomError(Exception):
    pass


x = "hello"
if not isinstance(x, int):
    raise MyCustomError("x must be an integer!")
