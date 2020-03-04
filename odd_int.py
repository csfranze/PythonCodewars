#Given an array, find the integer that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

def find_it(seq):
    my_dictionary = {i:seq.count(i) for i in seq}
    for key in my_dictionary:
        if my_dictionary[key] % 2 == 1:
            return(key)
