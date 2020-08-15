"""Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)
"""


def max_divider(incoming_num):
    counter1 = 1
    counter2 = 1
    while incoming_num >= counter1:
        counter1 = counter1 * 2
        if incoming_num % counter1 == 0:
            counter2 = counter1
    return counter2


print(max_divider(16))
