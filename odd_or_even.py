#Given an vector of numbers, determine whether the sum of all of the numbers is odd or even.
#
#Example:
#odd_or_even(vec![0]) returns "even"
#odd_or_even(vec![0, 1, 4]) returns "odd"
#odd_or_even(vec![0, -1, -5]) returns "even"

def oddOrEven(arr):
    s = [ ]
    if sum(arr) % 2 == 0:
        s.append('even')
    else:
        s.append('odd')
    answer = ' '.join(map(str, s))
    return(answer)
