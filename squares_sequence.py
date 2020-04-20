Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number. If n is negative or zero, return an empty array/list.

Examples

2, 5  -->  [2, 4, 16, 256, 65536]
3, 3  -->  [3, 9, 81]


def squares(x, n):
    arr = []
    sq = x
    while len(arr) < n:
        arr.append(sq)
        sq = sq**2
    return arr
