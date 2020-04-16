# For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

# E. g.,

# last_digit([3, 4, 2]) == 1
# because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

# Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

# Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.


def last_digit(arr):
    # Prune the zeros in the array.
    while (0 in arr) and (len(arr) > 2):
        for index in range(len(arr)-1, -1, -1):
            if arr[index] == 0:
                arr = arr[:index-1]
                break
    # Deal with the remaining pruned array.
    if len(arr) == 0:
        return 1
    elif len(arr) == 1:
        return arr[0] % 10
    elif len(arr) == 2:
        return pow(arr[0], arr[1], 10)
    elif len(arr) > 2:
        b = arr[0] % 10  # next, reduce the base mod 10
        if b == 0 or b == 1 or b == 5 or b == 6:
            return b  # these bases have period 1
        elif b == 4 or b == 9:
            e = arr[1] % 2  # these bases have period 2
            if e == 0:
                e = 2  # exponent should be non-zero
            return (b**e) % 10
        else:
            e = pow(arr[1], arr[2], 4)  # these bases have period 4
            if e == 0:
                e = 4  # exponent should be non-zero
            return (b**e) % 10
