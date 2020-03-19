#How many ways can you make the sum of a number?

#From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

#In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:
#4
#3 + 1
#2 + 2
#2 + 1 + 1
#1 + 1 + 1 + 1
#Examples

#Basic

#exp_sum(1) # 1
#exp_sum(2) # 2  -> 1+1 , 2
#exp_sum(3) # 3 -> 1+1+1, 1+2, 3
#exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
#exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

#exp_sum(10) # 42
#Explosive

#exp_sum(50) # 204226
#exp_sum(80) # 15796476
#exp_sum(100) # 190569292

import sys
""" Set new (higher) recursion limit. """
sys.setrecursionlimit(int(1e6))

def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def p(n,k):
    """ Partition of n into k distinct parts. """
    if n == 0 and k == 0:
        return 1
    elif (n == 0 and k != 0) or (n != 0 and k == 0) or (n < k):
        return 0
    else:
        return p(n-k,k)+p(n-1,k-1)

def exp_sum(n):
    """ Number of partitions of n. """
    return sum([p(n,k) for k in range(1,n+1)])
