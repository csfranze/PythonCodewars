# Multiply all the digits of a nonnegative integer n by each other, repeating with the product until a single digit is obtained. The number of steps required is known as the multiplicative persistence.

# Create a function that calculates the individual results of each step, not including the original number, but including the single digit, and outputs the result as a list/array. If the input is a single digit, return an empty list/array.

# Examples

# per(1)  = []

# per(10) = [0]
# // 1*0 = 0

# per(69) = [54, 20, 0]
# // 6*9 = 54 --> 5*4 = 20 --> 2*0 = 0


import numpy as np


def per(n):
    digits = [int(i) for i in list(str(n))]
    arr = []
    while len(digits) > 1:
        arr.append(np.product(digits))
        digits = [int(i) for i in list(str(np.product(digits)))]
    return arr
