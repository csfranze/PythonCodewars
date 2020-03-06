#You have to create a function that takes a positive integer number and returns the next bigger number #formed by the same digits:

#12 ==> 21
#513 ==> 531
#2017 ==> 2071
#If no bigger number can be composed using those digits, return -1:

#9 ==> -1
#111 ==> -1
#531 ==> -1

def next_bigger(n):
    # Convert the number to an array of its digits and specify default value.
    n_arr = [int(str(n)[i]) for i in range(0,len(str(n)))]
    next_bgg = 0
    # Identify first instance where sequence of digits decreases, read right to left.
    # This recipient digit must be swapped for the minimum of the digits that occur after,
    # provided those digits are bigger than the recipient digit.
    for i in range(1,len(n_arr)):
        if n_arr[-i-1] < n_arr[-i]:
            recipient_digit = n_arr[-i-1]
            donor_digit = min([n_arr[-j] for j in range(1,i+1) if n_arr[-j]>n_arr[-i-1]])
            donor_digit_index = n_arr[::-1].index(donor_digit)
            n_arr[-i-1] = donor_digit
            n_arr[len(n_arr)-1-donor_digit_index] = recipient_digit
            # Once the digits have been swapped, reverse the digits after the recipient digit.
            n_arr_modified = n_arr[:-i:1]+n_arr[:-i-1:-1]
            next_bgg = int(''.join(str(digit) for digit in n_arr_modified))
            break
    if next_bgg > n:
        return next_bgg
    else:
        return -1
