# A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

# Write a function that computes the nth smallest Hamming number.

# Specifically:

# The first smallest Hamming number is 1 = 203050
# The second smallest Hamming number is 2 = 213050
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051
# The 20 smallest Hamming numbers are given in example test fixture.


def hamming(n):
    h = [1] * n
    p, q, r = 2, 3, 5
    i = j = k = 0
    for a in range(1, n):
        h[a] = min(p, q, r)
        if p == h[a]:
            i += 1
            p = 2 * h[i]
        if q == h[a]:
            j += 1
            q = 3 * h[j]
        if r == h[a]:
            k += 1
            r = 5 * h[k]
    return h[-1]
