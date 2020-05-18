"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
   цена, а также количество S товара Посчитайте общую цену в рублях и копейках
   за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
    m = m * s
    n = n * s
    if n > 100:
        k = n // 100
        n = n % 100
        m = m + k
    sum = str(m) + " rubles " + str(n) + " kopecks"
    return sum  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = '', '', ''
    print(total_sum(m, n, s))
