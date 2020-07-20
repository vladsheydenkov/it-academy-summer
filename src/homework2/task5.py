"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    # write your code here

    if n in (1, 2):
        return 1
    else:
        if not cache.get(n - 1):
            cache[n - 1] = fibonacci(n - 1)
        if not cache.get(n - 2):
            cache[n - 2] = fibonacci(n - 2)
    return cache.get(n - 1) + cache.get(n - 2)


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(fibonacci(n))

