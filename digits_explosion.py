# Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

# Examples

# Digits.Explode("312") = "333122"
# Digits.Explode("102269") = "12222666666999999999"


def explode(s):
    s_lst = list(s)
    s_digits = [int(i) for i in s_lst if int(i) != 0]
    return ''.join([str(i)*i for i in s_digits])
