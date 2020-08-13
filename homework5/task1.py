"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
from inspect import isfunction
from homework2 import alltasks
functions = {func: getattr(alltasks, func) for func in dir(alltasks)
             if not func.startswith("__")
             and isfunction(getattr(alltasks, func))}


def runner(*args):
    if len(args) == 0:
        for func in functions:
            print(functions[func]())
    else:
        for passed_arg in args:
            if passed_arg in functions:
                print(functions[passed_arg]())



runner("total_sum", 'fibonacci')
