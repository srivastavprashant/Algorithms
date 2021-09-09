# binary exponentiation
# Computing a^n in log n time instead of Regular O(N)
# can be used with any property which is Associative (X.Y).Z = X.(Y.Z)
"""
Example: 3^13= can be written as 3^ ((1101)base2) as 1101 is 13
So, 3^8 + 3^4 + 3^1 = 3^13 , here bit 2 is unset

So a^n= {   1             if n==0
        {   (a^(n/2) )^2  if n>0 and n even
        {   (a^((n-1)/2))^2 . a     if n>0 and n odd

 #Application refer cp-algo
 Effective computation of large exponents modulo a number
Effective computation of Fibonacci numbers
Applying a permutation k times
Fast application of a set of geometric operations to a set of points
Number of paths of length k in a graph
Variation of binary exponentiation: multiplying two numbers modulo m
"""


# recursive Method
def binpow(a, b):
    if b == 0:
        return 1
    res = binpow(a, b // 2)
    if b % 2 == 0:
        return res * res * a
    else:
        return res * res


# iterative use this mostly


def binpow(a, b):
    res = 1
    while b > 0:
        if b & 1 == 1:
            res = res * a
        a = a * a
        b >>= 1
    return res

#Compute x^n mod m
def binpow(a,b,m):
    a%=m
    res=1
    while b > 0:
        if b & 1 == 1:
            res = (res * a) %m
        a = (a * a)%m
        b >>= 1
    return res
#If m is a prime number we can speed up a bit this algorithm by calculating x^n mod(m−1) instead of  x^n


