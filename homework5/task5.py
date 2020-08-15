"""Написать программу которая находит ближайшую
степень двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def degree(incoming_num):
    counter = 1
    while incoming_num >= 2**counter:
        counter += 1
    return counter - 1
