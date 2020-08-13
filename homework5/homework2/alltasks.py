import string


def total_sum(m = 1, n = 2, s = 3):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
    cost = s * (100 * m + n)
    return str(cost // 100) + " rubles " + str(cost % 100) + " kopecks"


def longest_word(str_ = "slklkgfsajl'"):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
    """

    # write your code here
    for mark in string.punctuation:
        str_ = str_.replace(mark, "")
    str_ = str_.split()
    longest_word = str_[0]
    for word in str_:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def sub_string(str_ = "sdall//./.jnvsoc"):
    """Конструирование подстроки.

    :param str_: входная строка
    :return: строка. Получившееся выражение
    """

    # write your code here
    new_str_ = ""
    marks = ['.', ',', '!', '?', '-', ':', '(', ')', '"', '\'', ';', ' ']
    for symbol in str_:
        if symbol not in marks and symbol not in new_str_:
            new_str_ += symbol
    return new_str_


def count_letters(str_ = "s;lkfjv'oidioavi i ij ij pij p"):
    """Подсчет символов.

    :param str_: входная строка
    :return: кортеж. (low_number, up_number). low_number - количество строчных,
                                              up_number - количество пописных.
    """

    # write your code here
    low_number = 0
    up_number = 0
    for i in str_:
        if i.isupper():
            up_number += 1
        elif i.islower():
            low_number += 1
    return (low_number, up_number)  # write return value here


def fibonacci(n = 10):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    # write your code here
    fib1 = fib2 = 1
    n = n - 2
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    return fib2


def palindrom(n = 102):
    """Поиск числа фибоначчи.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    # write your code here
    x = 0
    while n > 0:
        x = (x * 10) + n % 10
        n = n // 10
    if n == x:
        return True
    else:
        return False
