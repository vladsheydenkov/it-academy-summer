"""Даны два списка чисел. Посчитайте, сколько различных
чисел содержится одновременно как в первом списке, так и во втором.
"""
list_1 = [2, 3, 4, 6, 7, 2, 3, 0]
list_2 = [3, 11, 32, 56, 3, 9]
new_list = []
for num1 in list_1:
    if num1 in list_2 and num1 not in new_list:
        new_list.append(num1)
print(len(new_list))
