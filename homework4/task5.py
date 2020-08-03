"""Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi,
после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
Выходные данные
В первой строке выведите количество языков,
которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""
from functools import reduce


def compare(first, second):
    return set.intersection(set(first), set(second))


languages = []
with open("students.txt") as s:
    for num_of_s in range(int(s.readline())):
        languages.append([])
        for M1 in range(int(s.readline())):
            language = s.readline().strip()
            languages[num_of_s].append(language)
all_known = reduce(compare, languages)
all_languages = set()
for lists in languages:
    all_languages.update(set(lists))
print(len(all_languages))  # number of languages that all students know
for i in all_languages:
    print(i)  # list of languages that all students know
print(len(all_known))  # number of languages every student knows
print(*all_known)  # list of languages every student knows
