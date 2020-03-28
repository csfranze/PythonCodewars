# Given an integer, if the length of it's digits is a perfect square, return a square block of sqroot(length) * sqroot(length). If not, simply return "Not a perfect square!".

# Examples:

# 1212 returns:

# 12
# 12
# Note: 4 digits so 2 squared (2x2 perfect square). 2 digits on each line.

# 123123123 returns:

# 123
# 123
# 123
# Note: 9 digits so 3 squared (3x3 perfect square). 3 digits on each line.

import math


def square_it(digits):
    digits_lst = list(str(digits))
    M = len(digits_lst)
    N = math.sqrt(M)
    I = int(N)
    if N - I == 0:
        if I == 1:
            return(''.join(digits_lst))
        else:
            for i in range(I, M+1, I+1):
                digits_lst.insert(i, '\n')
            return(''.join(digits_lst))
    else:
        return('Not a perfect square!')
