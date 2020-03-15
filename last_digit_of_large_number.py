#Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

#For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6. Also, please take 0^0 to be 1.

#You may assume that the input will always be valid.

#Examples

#last_digit(4, 1)                # returns 4
#last_digit(4, 2)                # returns 6
#last_digit(9, 7)                # returns 9
#last_digit(10, 10 ** 10)        # returns 0
#last_digit(2 ** 200, 2 ** 300)  # returns 6

def last_digit(n1, n2):
    if n2 == 0: # first, dispense with the trivial case n2=0
        return 1
    b = n1 % 10 # next, reduce the base mod 10
    if b == 0 or b == 1 or b == 5 or b == 6:
        return b # these bases have period 1
    elif b == 4 or b == 9:
        e = n2 % 2 # these bases have period 2
        if e == 0:
            e = 2 # exponent should be non-zero
        return (b**e) % 10
    else:
        e = n2 % 4 # these bases have period 4
        if e == 0:
            e = 4 # exponent should be non-zero
        return (b**e) % 10
