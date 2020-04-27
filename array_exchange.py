# Array Exchange and Reversing

# It's time for some array exchange! The objective is simple: exchange the elements of two arrays in-place in a way that their new content is also reversed.

# before
# my_list = ['a', 'b', 'c']
# other_list = [1, 2, 3]

# exchange_with(my_list, other_list)

# after
# my_list == [3, 2, 1]
# other_list == ['c', 'b', 'a']


def exchange_with(a, b):
    temp_1 = a[::-1]
    temp_2 = b[::-1]
    a.reverse()
    b.reverse()
    a.extend(b)
    b.extend(temp_1)
    del a[0:len(temp_1)]
    del b[0:len(temp_2)]
