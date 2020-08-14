"""Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел,
отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""
from functools import reduce

initial_list = [0, 1, 2, 3, 4, 7, 8, 10]


def get_ranges(list_):
    answer = [str(list_[0])]
    print(answer)
    x = 0
    y = 1
    while y <= len(list_) - 1:
        if list_[x] + 1 != list_[y]:
            answer.append(str(list_[x]))
            answer.append(str(list_[y]))
        x += 1
        y += 1
    answer.append(str(list_[-1]))
    print(answer)
    string_ = ""
    for sym in answer:
        if answer.count(sym) == 2:
            double = answer.index(sym)
            answer.pop(double + 1)
            answer[double] = answer[double] + ","
    print(answer)

    another_list = []
    pars = []
    for num in answer:
        if "," not in num:
            another_list.append(num)
            print(another_list)
            if len(another_list) == 2:
                print(another_list)
                b = another_list[:]
                pars.append(b)
                another_list.clear()
                print(another_list)
        else:
            pars.append(num)
    print(pars)

    for sublist in pars:
        if type(sublist) == list:
            string_answer += (sublist[0] + "-" + sublist[1] + ",")
        else:
            string_answer += sublist

    string_answer = string_.strip("-,")
    print(string_answer)


get_ranges(initial_list)
