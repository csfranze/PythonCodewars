Create a function that returns an array containing the first l digits from the nth diagonal of Pascal's triangle.

n = 0 should generate the first diagonal of the triangle (the 'ones'). The first number in each diagonal should be 1.

If l = 0, return an empty array. Assume that both n and l will be non-negative integers in all test cases.


from scipy.special import binom


def generate_diagonal(n, l):
    return [round(binom(n+i, n)) for i in range(0, l)]
