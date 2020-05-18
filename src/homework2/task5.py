"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    # write your code here
    fibonachi_list = [1, 2]
    for i in range(1, n-1):
        x = (fibonachi_list[-2] + fibonachi_list[-1])
        fibonachi_list.append(x)

    return fibonachi_list[n-1]  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(fibonacci(n))
