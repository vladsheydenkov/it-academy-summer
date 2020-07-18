"""Найти самое длинное слово в введенном предложении. В случае если их
    несколько, самое левое в строке Учтите что в предложении есть знаки
    препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
    """

    # write your code here
    import string
    for mark in string.punctuation:
        str_ = str_.replace(mark, "")
    str_ = str_.split()
    longest_word = str_[0]
    for string in str_:
        if len(string) > len(longest_word):
            longest_word = string
    return longest_word


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))