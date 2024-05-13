def greate_operation(operation):
    if operation == "multiplication":
        def multiplication(x, y):
            return x * y

        return multiplication
    elif operation == "division":

        def division(x, y):
            return x // y

        return division


my_func_1 = greate_operation("multiplication")
print(my_func_1(1, 2))

my_func_1 = greate_operation("division")
print(my_func_1(6, 3))

multiply = (lambda x, y: x ** y)
print(multiply(7, 2))


def multiply_1(x, y):
    return x ** y


print(multiply_1(7, 2))


class Rest:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return b * self.a


area_of_a_rectangle = Rest(12)
result = area_of_a_rectangle(10)
print(result)
