"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
from homework2 import alltasks as a
from inspect import isfunction

functions = {func: getattr(a, func)
             for func in dir(a) if not
             func.startswith("__") and isfunction(getattr(a, func))}


def runner(*args):
    if len(args) == 0:
        for func in functions:
            print(functions[func]())
    else:
        for passed_arg in args:
            if passed_arg in functions:
                print(functions[passed_arg]())


runner("total_sum", 'fibonacci')
