'''
Created on 2022/12/05

'''

import collections


def prime_factorize(n):
    a = []

    while n % 2 == 0:
        a.append(2)
        n //= 2

    f = 3

    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        a.append(n)

    if len(a) == 0:
        a.append(1)

    return a


K = int(input())

c = collections.Counter(prime_factorize(K))

max = 1

for key, value in c.items():
    if max < key * value:
        max = key * value

print(max)
