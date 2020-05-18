"""Найти самое длинное слово в введенном предложении. В случае если их
    несколько, самое левое в строке Учтите что в предложении есть знаки
    препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    # write your code here
    new_str_ = ""
    marks = ['.', ',', '!', '?', '-', ':', '(', ')', '"', '\'', ';']
    for symbol in str_:
        if symbol not in marks:
            new_str_ += symbol

    new_str_ = new_str_.split()
    longest_word = new_str_[0]
    for string in new_str_:
        if len(string) > len(longest_word):
            longest_word = string
    print(longest_word)
    return longest_word


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))
