#A happy number is one where if you repeatedly square its digits and add them together, you eventually end up at 1.

#For example:

#7 -> 49 -> 97 -> 130 -> 10 -> 1 so 7 is a happy number.

#42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 so 42 is not a happy number.

#This can also be done with powers other than 2.

#Complete the function that receives 2 arguments: the starting number and the exponent. It should return an array of numbers containing whatever loop it encounters, or [1] if it doesn't encounter any. This array should only include the numbers in the loop, not any that lead into the loop, and should repeat the first number as the last number e.g.:

#[42, 20, 4, 16, 37, 58, 89, 145, 42]
#The first number in the array should be where the loop is first encountered.

#All function inputs will be positive integers, with the exponent being between 2 and 4.

def is_happy(n, pow):
    n_arr = [int(str(n)[i]) for i in range(0,len(str(n)))]
    n_sq_sum = sum([i**pow for i in n_arr])
    results = [n]
    while n_sq_sum > 0:
        results.append(n_sq_sum)
        if n_sq_sum == 1:
            return([1])
            break
        else:
            new_n_arr = [int(str(n_sq_sum)[i]) for i in range(0,len(str(n_sq_sum)))]
            new_sq_sum = sum([i**pow for i in new_n_arr])
            n_sq_sum = new_sq_sum
            if n_sq_sum not in results:
                pass
            else:
                results.append(n_sq_sum)
                loop_start = results.index(n_sq_sum)
                return(results[loop_start:])
                break
