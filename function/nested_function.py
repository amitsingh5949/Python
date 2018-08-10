# nested function


def outer_function():
    lst = [1, 2, 3, 4, 5]

    def inner_function():
        for x in lst:
            print(x)
    inner_function()


outer_function()
