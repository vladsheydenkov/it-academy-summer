"""Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""


def dec(func_):
    cache = []

    def wrapper(*args, **kwargs):
        nonlocal cache
        res = func_(*args, **kwargs)
        cache.append(res)
        f = open('logs.txt', 'a')
        f.write(str(cache))
        f.close()
        return cache
    return wrapper


@dec
def func_(*input_):
    return input_


print(func_("lala"))
print(func_("lalalala"))
print(func_("lalalalalala"))
