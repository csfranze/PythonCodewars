In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.

from itertools import permutations as permute
import math
import functools
import operator

def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str

def permutations(string):
    return list(map(convertTuple,list(set(list(permute(string))))))
