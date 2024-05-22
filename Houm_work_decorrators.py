import math


def is_primee(func):
    def wrapper(a, b, c):
        print('Считаем сумму трёх чисел')
        func(a, b, c)
        print('Проверяем число')
    return wrapper


@is_primee
def sum_three(a, b, c):
    total = a + b + c
    print(total)
    return


sum_three(1, 1, 1)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


num = 3
if is_prime(num):
    print(f"{num} - простое.")
else:
    print(f"{num} - составное.")
