# Task

# Given a positive integer as input, return the output as a string in the following format:

# Each element, corresponding to a digit of the number, multiplied by a power of 10 in such a way that with the sum of these elements you can obtain the original number.

# Examples

# Input	Output
# 0	""
# 56	"5*10+6"
# 60	"6*10"
# 999	"9*100+9*10+9"
# 10004	"1*10000+4"


def simplify(number):
    number_lst = list(str(number))
    place_vals = [str(10**j) for j in range(len(number_lst)-1, -1, -1)]

    s = ''
    for i in range(0, len(number_lst)-1):
        if int(number_lst[i]) != 0:
            s = s + number_lst[i] + '*' + place_vals[i] + '+'

    if int(number_lst[-1]) == 0 and len(number_lst) == 1:
        return s
    elif int(number_lst[-1]) == 0 and len(number_lst) > 1:
        return s[:-1]
    else:
        s = s + number_lst[-1]
        return s
