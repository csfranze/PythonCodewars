# Write a function that takes an array/list of numbers and returns a number.

# See the examples and try to guess the pattern:

# even_odd([1,2,6,1,6,3,1,9,6]) => 393
# even_odd([1,2,3]) => 5
# even_odd([0,2,3]) => 3
# even_odd([1,0,3]) => 3
# even_odd([3,2])   => 6


def even_odd(arr):
    res = arr[0]
    if len(arr) % 2 == 0:
        arr.append(0)
    for i in range(0,len(arr)-2,2):
        res = res * arr[i+1] + arr[i+2]
    return res
