# Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits in the given string of digits.

# For example:

# greatestProduct("123834539327238239583") // should return 3240
# The input string always has more than five digits.

import numpy as np


def greatest_product(n):
    n_arr = [int(j) for j in list(n)]
    products = []
    for i in range(0, len(n)-4):
        products.append(np.product(n_arr[i:i+5]))
    return max(products)
