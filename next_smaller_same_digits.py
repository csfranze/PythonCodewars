# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# For example:

# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.


def next_smaller(n):
    print(n)
    # Convert the number to an array of its digits and specify default value.
    n_arr = [int(str(n)[i]) for i in range(0, len(str(n)))]
    next_sm = 0
    # Identify first instance where sequence of digits increase, read right to left.
    # This recipient digit must be swapped for the maximum of the digits that occur after,
    # provided those digits are smaller than the recipient digit.
    for i in range(1, len(n_arr)):
        if n_arr[-i-1] > n_arr[-i]:
            recipient_digit = n_arr[-i-1]
            donor_digit = max([n_arr[-j] for j in range(1,i+1) if n_arr[-j] < n_arr[-i-1]])
            donor_digit_index = n_arr[::-1].index(donor_digit)
            n_arr[-i-1] = donor_digit
            n_arr[len(n_arr)-1-donor_digit_index] = recipient_digit
            # Once the digits have been swapped, reverse the digits after the recipient digit.
            n_arr_modified = n_arr[:-i:1]+n_arr[:-i-1:-1]
            next_sm_str = ''.join(str(digit) for digit in n_arr_modified)
            next_sm = int(next_sm_str)
            break
    if next_sm < n and len(str(next_sm)) == len(str(n)) and next_sm != 0:
        return next_sm
    else:
        return -1
