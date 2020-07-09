"""If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000
"""
# var 1
x = 0
for i in range(1, 1001):
    if not i % 3 or not i % 5:
        x += i
print(x)


# var 2
y = [s for s in range(1001) if not s % 3 or not s % 5]
print(sum(y))


"""Each new term in the Fibonacci sequence is generated
by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence
whose values do not exceed four million,
find the sum of the even-valued terms."""
# var 1
su = 0
x = 0
y = 1
while x < 4000000 and y < 4000000:
    x += y
    if not x % 2:
        su += x
    y += x
    if not y % 2:
        su += y
print(su)


# var 2
m = [1, 2]
while m[-1] < 4000000:
    m.append(m[-2] + m[-1])


def filt(a):
    if not a % 2:
        return a


b = filter(filt, m)
print(sum(b))


# var 3
m = [1, 2]
while m[-1] < 4000000:
    m.append(m[-2] + m[-1])
b = filter(lambda a: not a % 2, m)
print(sum(b))


"""You are given an array
(which will have a length of at least 3, but could be very large)
containing integers.
The array is either entirely comprised of odd integers
or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument
and returns this "outlier" N.
"""


def find_outlier(integers):
    listEven = []
    listOdd = []
    for num in integers:
        if num % 2 == 0:
            listEven.append(num)
        else:
            listOdd.append(num)

    if len(listEven) == 1:
        return listEven[0]
    else:
        return listOdd[0]
